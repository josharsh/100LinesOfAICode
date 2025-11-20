# 📚 Mini RAG

**Chat with your documents** - Answers questions using your files as knowledge.

## Quick Start

```bash
pip install anthropic numpy
export ANTHROPIC_API_KEY=your_key

python rag.py index ./docs
python rag.py query "What is this project about?"
```

## How It Works

1. **Index**: Split documents into chunks → Create embeddings → Store in memory
2. **Search**: Convert query → Find similar chunks via cosine similarity
3. **Answer**: Pass relevant chunks to Claude → Get cited answer

**Example Output:**
```
❓ Question: What are the main features?

💡 Answer:
Based on Document 1, the main features are:
1. Document indexing with semantic search
2. Question answering with source citations
3. No external vector DB dependencies
```

## Programmatic Use

```python
from rag import MiniRAG

rag = MiniRAG()
rag.add_directory("./docs")
answer = rag.query("How do I configure logging?")
rag.save("my_kb.json")
```

**94 lines. No vector DB needed.**
