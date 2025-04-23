from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
from config.settings import OPENAI_API_KEY
from tools.my_calc import my_calc_tool
from tools.reverse_text import reverse_text_tool

def create_agent():
    llm = OpenAI(temperature=0, api_key=OPENAI_API_KEY)

    tools = [my_calc_tool, reverse_text_tool]

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )

    return agent
