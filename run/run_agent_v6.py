import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v6_retriever import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 6 – ToolRetriever + Embedding-Based Tool Selection")
    slow_print("In this stage, your agent becomes smarter by using embeddings to dynamically select tools.")
    slow_print("Instead of considering all tools every time, it uses ChromaDB to semantically filter relevant ones.")
    slow_print("--------------------------------------------------")
    slow_print("🔧 Setting up the embedding-aware agent with Chroma vector store...")

    agent = create_agent()

    slow_print("✅ Agent is ready with tool retrieval logic.")
    slow_print("Let's test how it routes queries based on semantic similarity.\n")

    slow_print("🔢 Example 1: What is 42 * 1.5?")
    print(agent.invoke({"input": "What is 42 * 1.5?"}))

    slow_print("\n🔄 Example 2: Repeat after me: LangChain is cool")
    print(agent.invoke({"input": "Repeat after me: LangChain is cool"}))

    slow_print("\n🧠 Concept Recap:")
    slow_print("""
- This stage uses LangChain’s ToolRetriever with vector search.
- Each tool’s description is embedded using SentenceTransformers.
- User queries are embedded and compared to find the top-k relevant tools.
- The agent only reasons over those tools — making it scalable and contextually smarter.
- We used ChromaDB as the in-memory vector store for embeddings.
    """)

    slow_print("📂 To see how this is implemented, explore:")
    slow_print("→ tools/retriever.py")
    slow_print("→ agents/agent_v6_retriever.py\n")

    slow_print("✅ You've completed Stage 6. Try adjusting tool descriptions or adding new tools to see how routing adapts!")

if __name__ == "__main__":
    run_demo()