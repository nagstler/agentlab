import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agent_v5_functions import create_agent

if __name__ == "__main__":
    agent = create_agent()

    print(agent.invoke({"input": "Please add 45 and 55"}))
    print(agent.invoke({"input": "Now multiply that result by 3"}))
