from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
from tools.my_calc_structured import structured_calc_tool

def create_agent():
    llm = ChatOpenAI(temperature=0, api_key=OPENAI_API_KEY, model="gpt-4")

    tools = [structured_calc_tool]
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # ✅ Explicit variable declaration — fully compatible
    prompt = ChatPromptTemplate(
        input_variables=["input", "chat_history", "agent_scratchpad"],
        messages=[
            ("system", "You are a helpful assistant who uses tools when needed."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_openai_functions_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
    )

    return executor
