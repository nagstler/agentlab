import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v4_prompt import create_agent

if __name__ == "__main__":
    agent = create_agent()

    print(agent.invoke("What is 99 * 2?"))
    print(agent.invoke("Reverse the result, please."))
