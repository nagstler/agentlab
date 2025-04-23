import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v3_memory import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 3 – Memory")
    slow_print("In this stage, the agent is equipped with memory using `ConversationBufferMemory`.")
    slow_print("This allows it to remember previous inputs and respond based on past context.")
    slow_print("--------------------------------------------------")
    slow_print("🔧 Setting up the memory-enabled agent...")

    agent = create_agent()

    slow_print("✅ Agent is ready with memory support.")
    slow_print("Let's try a two-step math interaction and see if it remembers the previous result.\n")

    slow_print("🔢 Step 1: What is 15 * 3?")
    print(agent.invoke("What is 15 * 3?"))  # → 45

    slow_print("\n🔁 Step 2: Now multiply that result by 2")
    print(agent.invoke("Now multiply that result by 2"))  # Should understand "that result"

    slow_print("\n📌 Concept Recap:")
    slow_print("""
- This stage introduces `ConversationBufferMemory` to the agent.
- The memory stores prior inputs and outputs as part of the ongoing context.
- It enables multi-turn interactions, essential for building helpful assistants.
- The memory is injected using the `memory_key` into the prompt logic.
- You can now ask follow-up questions, and the agent will refer back to earlier turns.
    """)

    slow_print("📂 For implementation details, look at:")
    slow_print("→ agents/agent_v3_memory.py\n")

    slow_print("✅ You've completed Stage 3. Try extending memory use across 3 or 4 steps!")

if __name__ == "__main__":
    run_demo()