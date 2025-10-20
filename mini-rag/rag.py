#!/usr/bin/env python3
"""Minimal RAG - Chat with your documents in <100 lines."""
import os, sys, json
from pathlib import Path
from typing import List, Tuple
import numpy as np
from anthropic import Anthropic

class MiniRAG:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.documents: List[dict] = []
        self.embeddings: List[np.ndarray] = []

    def simple_embedding(self, text: str) -> np.ndarray:
        """Create simple word-frequency based embedding (no API needed)."""
        words = text.lower().split()
        vocab = sorted(set(words))
        vector = np.zeros(min(len(vocab), 100))
        for i, word in enumerate(vocab[:100]):
            vector[i] = words.count(word) / len(words)
        return vector / (np.linalg.norm(vector) + 1e-10)

    def add_document(self, content: str, metadata: dict = None):
        """Add a document to the knowledge base."""
        chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
        for chunk in chunks:
            self.documents.append({"content": chunk, "metadata": metadata or {}})
            self.embeddings.append(self.simple_embedding(chunk))

    def add_file(self, filepath: str):
        """Add a file to the knowledge base."""
        path = Path(filepath)
        self.add_document(path.read_text(), {"source": filepath, "filename": path.name})

    def add_directory(self, dirpath: str, extensions: List[str] = [".txt", ".md"]):
        """Add all files from directory."""
        for ext in extensions:
            for file in Path(dirpath).rglob(f"*{ext}"):
                try:
                    print(f"Adding {file}...")
                    self.add_file(str(file))
                except Exception as e:
                    print(f"Error adding {file}: {e}")

    def search(self, query: str, top_k: int = 3) -> List[Tuple[dict, float]]:
        """Search documents by similarity."""
        query_emb = self.simple_embedding(query)
        scores = [np.dot(query_emb, doc_emb) for doc_emb in self.embeddings]
        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [(self.documents[i], scores[i]) for i in top_indices]

    def query(self, question: str, top_k: int = 3) -> str:
        """Query the knowledge base."""
        results = self.search(question, top_k)
        context = "\n\n".join([f"Document {i+1} (relevance: {score:.2f}):\n{doc['content']}"
                               for i, (doc, score) in enumerate(results)])

        prompt = f"""Answer the question based on these documents:

{context}

Question: {question}

Instructions:
- Use ONLY information from the documents
- If answer not in documents, say "I don't have that information"
- Cite which document number you used
- Be concise and accurate

Answer:"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    def save(self, filepath: str):
        """Save knowledge base to file."""
        data = {"documents": self.documents, "embeddings": [e.tolist() for e in self.embeddings]}
        Path(filepath).write_text(json.dumps(data))

    def load(self, filepath: str):
        """Load knowledge base from file."""
        data = json.loads(Path(filepath).read_text())
        self.documents = data["documents"]
        self.embeddings = [np.array(e) for e in data["embeddings"]]

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python rag.py index <file|dir>    # Add documents")
        print("  python rag.py query '<question>'  # Ask a question")
        print("\nExample:")
        print("  python rag.py index docs/")
        print("  python rag.py query 'What is the main topic?'")
        sys.exit(1)

    rag = MiniRAG()
    kb_file = "knowledge_base.json"

    if Path(kb_file).exists():
        rag.load(kb_file)
        print(f"✓ Loaded knowledge base ({len(rag.documents)} documents)")

    command = sys.argv[1]

    if command == "index":
        path = sys.argv[2]
        if Path(path).is_file():
            rag.add_file(path)
        else:
            rag.add_directory(path)
        rag.save(kb_file)
        print(f"✓ Indexed {len(rag.documents)} document chunks")

    elif command == "query":
        question = sys.argv[2]
        answer = rag.query(question)
        print(f"\n❓ Question: {question}\n")
        print(f"💡 Answer:\n{answer}")

if __name__ == "__main__":
    main()
