from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
from langchain_openai import OpenAI
from config.settings import OPENAI_API_KEY

def create_agent():
    llm = OpenAI(temperature=0, api_key=OPENAI_API_KEY)
    tools = load_tools(["llm-math"], llm=llm)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
