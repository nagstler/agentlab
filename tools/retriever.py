from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.tools import Tool

from tools.my_calc import my_calc_tool
from tools.reverse_text import reverse_text_tool
from tools.echo import echo_tool

def get_filtered_tools(query: str, top_k=2):
    tools = [my_calc_tool, reverse_text_tool, echo_tool]

    # Convert tool descriptions to vector documents
    docs = [Document(page_content=tool.description, metadata={"tool": tool.name}) for tool in tools]

    # Embed descriptions and store in Chroma
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding=embeddings)

    # --- Inspect the vector store ---
    print("VECTOR STORE: Listing all tool descriptions stored:")
    all_docs = vectorstore.similarity_search("list all", k=10)
    for idx, doc in enumerate(all_docs):
        print(f"Tool {idx+1}:")
        print(f"Content: {doc.page_content}")
        print(f"Metadata: {doc.metadata}")
        print("-" * 40)


    retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})

    # Retrieve top-k descriptions and match to tools
    results = retriever.get_relevant_documents(query)
    relevant_tool_names = [doc.metadata["tool"] for doc in results]

    return [tool for tool in tools if tool.name in relevant_tool_names]
