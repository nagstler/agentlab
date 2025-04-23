import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v5_functions import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 5 – Function-Calling Agent (Structured Tools)")
    slow_print("In this stage, we integrate OpenAI's function calling via `StructuredTool`.")
    slow_print("The agent now interprets inputs into typed arguments and calls a structured backend function.")
    slow_print("--------------------------------------------------")
    slow_print("🔧 Setting up the function-calling agent with memory...")

    agent = create_agent()

    slow_print("✅ Agent is ready with structured tool support.")
    slow_print("Let's run a two-turn conversation using typed math functions.\n")

    slow_print("➕ Step 1: Please add 45 and 55")
    print(agent.invoke({"input": "Please add 45 and 55"}))

    slow_print("\n✖️ Step 2: Now multiply that result by 3")
    print(agent.invoke({"input": "Now multiply that result by 3"}))

    slow_print("\n📌 Concept Recap:")
    slow_print("""
- This stage introduces structured function calls using `StructuredTool`.
- The agent now parses inputs like 'x', 'y', and 'operator' for a calculator tool.
- It uses OpenAI’s function-calling protocol (via GPT-4) to ensure arguments are passed cleanly.
- The prompt was updated using `ChatPromptTemplate`, and memory is preserved via `ConversationBufferMemory`.
- This is more reliable and scalable than natural language tool invocation — ideal for production systems.
    """)

    slow_print("📂 For implementation insights, check:")
    slow_print("→ tools/my_calc_structured.py")
    slow_print("→ agents/agent_v5_functions.py\n")

    slow_print("✅ You've completed Stage 5. Try adding more structured tools or inspect the tool schema!")

if __name__ == "__main__":
    run_demo()