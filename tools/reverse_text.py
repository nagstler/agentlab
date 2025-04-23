from langchain.tools import Tool

def reverse_string(text: str) -> str:
    return text[::-1]

reverse_text_tool = Tool(
    name="reverse_text",
    func=reverse_string,
    description="Use this to reverse any input string. Example: 'hello' → 'olleh'"
)
