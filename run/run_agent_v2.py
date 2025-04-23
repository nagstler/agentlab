import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v2_multitool import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 2 – Multi-Tool Agent")
    slow_print("In this stage, our agent is enhanced with multiple tools.")
    slow_print("It can now intelligently decide whether to use a calculator or a reverse-text tool.")
    slow_print("--------------------------------------------------")
    slow_print("🔧 Initializing the multi-tool agent...")

    agent = create_agent()

    slow_print("✅ Agent is ready with two tools: `my_calc` and `reverse_text`.")
    slow_print("Let's test how the agent selects the right tool for different tasks.\n")

    slow_print("🧮 Question 1: What is 19 * 4.2?")
    print(agent.invoke("What is 19 * 4.2?"))

    slow_print("\n🔄 Question 2: Please reverse the word LangChain")
    print(agent.invoke("Please reverse the word LangChain"))

    slow_print("\n📌 Concept Recap:")
    slow_print("""
- In Stage 2, we combine multiple tools into one agent setup.
- LangChain agents use tool descriptions to decide which one to invoke.
- The agent uses the ReAct loop to reason about which tool fits the query.
- `my_calc` handles arithmetic questions, while `reverse_text` manipulates strings.
- This demonstrates how agents can become versatile by composing logic from multiple tools.
    """)

    slow_print("📂 Explore the implementation in:")
    slow_print("→ tools/my_calc.py")
    slow_print("→ tools/reverse_text.py")
    slow_print("→ agents/agent_v2_multitool.py\n")

    slow_print("✅ You've completed Stage 2. Try adding a third tool to explore further!")

if __name__ == "__main__":
    run_demo()