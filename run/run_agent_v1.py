import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v1_custom_tool import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 1 – Custom Tool: `my_calc`")
    slow_print("In this stage, we replace the default `llm-math` tool with our own custom calculator.")
    slow_print("This is the first step to learning how to build and inject tools into an agent.")
    slow_print("--------------------------------------------------")
    slow_print("🔧 Initializing the agent with our custom math tool: `my_calc`...")

    agent = create_agent()

    slow_print("✅ Agent is ready.")
    slow_print("📝 Question: What is 23.5 * 99?")
    slow_print("Let’s observe how the agent uses the custom `my_calc` tool...")

    result = agent.invoke("What is 23.5 * 99?")
    
    slow_print("🤖 Agent says:")
    print(result)
    
    slow_print("\n📌 Concept Recap:")
    slow_print("""
- In this stage, we introduce a custom LangChain Tool called `my_calc`.
- This tool is a simple Python function that evaluates math expressions locally.
- We wrap this function using LangChain’s `Tool` class, giving it a name and description.
- The agent uses our tool instead of calling an LLM-powered calculator.
- This helps you understand how to modularly add any business logic into your agent workflow.
- It also saves token usage and speeds up execution by avoiding unnecessary LLM calls.
    """)

    slow_print("📂 To see how this is implemented, check:")
    slow_print("→ tools/my_calc.py")
    slow_print("→ agents/agent_v1_custom_tool.py\n")

    slow_print("✅ You've completed Stage 1. Try modifying `my_calc` or adding another tool!")

if __name__ == "__main__":
    run_demo()