from langchain.tools import Tool

def simple_calculator(query: str) -> str:
    """Safely evaluate basic math expressions."""
    try:
        # Warning: eval is dangerous in prod. Replace with sympy in real apps.
        result = eval(query, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

my_calc_tool = Tool(
    name="my_calc",
    func=simple_calculator,
    description="Use this for basic math calculations like '23.5 * 99' or '100 / 4'"
)
