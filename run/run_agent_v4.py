import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v4_prompt import create_agent

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

def run_demo():
    slow_print("🧠 Welcome to AgentLab: Stage 4 – Custom Prompt Template")
    slow_print("This stage introduces prompt customization — a way to control your agent's personality and behavior.")
    slow_print("We'll use a sarcastic assistant persona named 'Marvin'.")
    slow_print("--------------------------------------------------")
    slow_print("🛠️ Initializing the memory-enabled agent with a custom prompt...")

    agent = create_agent()

    slow_print("✅ Agent is ready with Marvin's personality.")
    slow_print("Let's ask it to do some math and then manipulate the result.\n")

    slow_print("🧮 Step 1: What is 99 * 2?")
    print(agent.invoke("What is 99 * 2?"))

    slow_print("\n🔁 Step 2: Reverse the result, please.")
    print(agent.invoke("Reverse the result, please."))

    slow_print("\n📌 Concept Recap:")
    slow_print("""
- This stage shows how to modify the agent’s default system prompt using `agent_kwargs`.
- By customizing the prompt's `prefix`, we can change how the agent talks, thinks, and reacts.
- In this example, Marvin is a sarcastic assistant with memory and tool access.
- Prompt engineering plays a huge role in shaping agent tone, decision-making, and tool usage.
- This lets you personalize agents for different audiences or use cases.
    """)

    slow_print("📂 For implementation details, explore:")
    slow_print("→ agents/agent_v4_prompt.py\n")

    slow_print("✅ You've completed Stage 4. Try redefining Marvin’s tone or adding example messages!")

if __name__ == "__main__":
    run_demo()