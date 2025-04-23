import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v2_multitool import create_agent

if __name__ == "__main__":
    agent = create_agent()

    print("🧮 Math question:")
    print(agent.invoke("What is 19 * 4.2?"))

    print("\n🔄 Reverse text:")
    print(agent.invoke("Please reverse the word LangChain"))
