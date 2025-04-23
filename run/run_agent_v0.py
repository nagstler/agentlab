import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v0_basic import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 0 – Basic Agent")
    slow_print("In this stage, we explore the fundamentals of a LangChain agent using the ReAct paradigm.")
    slow_print("You'll see how an agent uses tools intelligently rather than just answering with raw LLM output.")
    slow_print("--------------------------------------------------")
    slow_print("🔧 Setting up the agent...")

    agent = create_agent()

    slow_print("✅ Agent is ready.")
    slow_print("📝 Question: What is 23.5% of 99?")
    slow_print("Let’s observe how the agent approaches this with tool-assisted reasoning...")

    result = agent.invoke("What is 23.5% of 99?")
    
    slow_print("🤖 Agent says:")
    print(result)
    
    slow_print("\n📌 Concept Recap:")
    slow_print("""
- This agent follows the ReAct pattern: it can Reason, Act (via a tool), and then return the result.
- The agent does not try to answer directly—it decides first whether it needs to call a tool.
- The tool used here is `llm-math`, which enables the agent to solve math problems using the LLM.
- LangChain wraps this logic in the `AgentExecutor` using an LLM + a list of tools + a default prompt template.
- This pattern is useful when you want your agents to make decisions, not just generate completions.
    """)

    slow_print("📂 To understand how the agent is constructed, refer to:")
    slow_print("→ agents/agent_v0_basic.py")

    slow_print("✅ You've completed Stage 0. Try changing the input to experiment further!")

if __name__ == "__main__":
    run_demo()