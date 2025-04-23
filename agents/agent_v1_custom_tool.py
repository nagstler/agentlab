from langchain.agents import initialize_agent, AgentType
from langchain_openai import OpenAI
from config.settings import OPENAI_API_KEY
from tools.my_calc import my_calc_tool

def create_agent():
    llm = OpenAI(temperature=0, api_key=OPENAI_API_KEY)
    tools = [my_calc_tool]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
