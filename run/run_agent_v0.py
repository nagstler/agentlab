import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v0_basic import create_agent

if __name__ == "__main__":
    agent = create_agent()
    result = agent.invoke("What is 23.5% of 99?")

    print("Agent says:", result)
