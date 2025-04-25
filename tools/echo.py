from langchain.tools import Tool

def echo_tool_fn(text: str) -> str:
    return f"You said: {text}"

echo_tool = Tool(
    name="echo_tool",
    func=echo_tool_fn,
    description="Echoes back the user's input. Use for reflecting/parroting input text."
)
