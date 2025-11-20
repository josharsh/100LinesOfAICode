#!/usr/bin/env python3
"""Stack Overflow in Your Terminal - Stay in flow, 78 lines"""
import os, sys, requests
from anthropic import Anthropic

class SOTerminal:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.so_api = "https://api.stackexchange.com/2.3/search/advanced"

    def search_stackoverflow(self, query: str) -> list:
        """Search Stack Overflow API."""
        try:
            params = {
                "order": "desc",
                "sort": "votes",
                "q": query,
                "site": "stackoverflow",
                "filter": "withbody"
            }
            response = requests.get(self.so_api, params=params, timeout=10)
            data = response.json()
            return data.get("items", [])[:3]  # Top 3 results
        except Exception:
            return []

    def format_answer(self, query: str, results: list) -> str:
        """Use AI to format and summarize SO results."""
        if not results:
            return "❌ No results found. Try rephrasing your query."

        # Prepare context from SO results
        context = ""
        for i, item in enumerate(results):
            context += f"\n--- Result {i+1} (Score: {item.get('score', 0)}) ---\n"
            context += f"Title: {item.get('title', 'N/A')}\n"
            context += f"Link: {item.get('link', 'N/A')}\n"
            context += f"Excerpt: {item.get('body', '')[:500]}\n"  # First 500 chars

        prompt = f"""User's question: {query}

Stack Overflow results:
{context}

Provide a concise, practical answer:

1. 📚 Best Answer: [Extract the most useful solution]
2. 💡 Code Example: [Show the code if available]
3. ⚠️ Important Notes: [Any caveats or variations]
4. 🔗 Source: [Which SO answer # to reference]

Keep it practical and terminal-friendly. Format code in plain text."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def interactive_search(self):
        """Interactive SO search session."""
        print("💡 Stack Overflow Terminal Search\n")
        print("Ask programming questions, get instant answers!")
        print("Type 'quit' to exit\n")
        print("═" * 50 + "\n")

        while True:
            query = input("🔍 Search: ").strip()

            if not query:
                continue

            if query.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Happy coding!\n")
                break

            print("\n🔎 Searching Stack Overflow...\n")

            results = self.search_stackoverflow(query)
            formatted = self.format_answer(query, results)

            print(formatted)
            print("\n" + "═" * 50 + "\n")

def main():
    if len(sys.argv) > 1:
        # Direct query mode
        query = " ".join(sys.argv[1:])
        so = SOTerminal()
        print(f"\n🔍 Searching: {query}\n")
        results = so.search_stackoverflow(query)
        print(so.format_answer(query, results))
        print()
    else:
        # Interactive mode
        so = SOTerminal()
        so.interactive_search()

if __name__ == "__main__":
    main()
