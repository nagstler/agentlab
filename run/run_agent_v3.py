import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v3_memory import create_agent

if __name__ == "__main__":
    agent = create_agent()

    print(agent.invoke("What is 15 * 3?"))  # → 45
    print(agent.invoke("Now multiply that result by 2"))  # Should understand "that result"
