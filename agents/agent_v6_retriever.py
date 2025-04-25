from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
from tools.retriever import get_filtered_tools

def create_agent():
    llm = ChatOpenAI(temperature=0, api_key=OPENAI_API_KEY, model="gpt-4")

    # Dynamically select relevant tools for this query
    query = "Please add 45 and 55"
    tools = get_filtered_tools(query)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    prompt = ChatPromptTemplate(
        input_variables=["input", "chat_history", "agent_scratchpad"],
        messages=[
            ("system", "You are a helpful assistant that dynamically selects tools."),
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
