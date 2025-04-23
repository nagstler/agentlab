from langchain.tools import StructuredTool

def calculate(x: float, y: float, operator: str) -> float:
    if operator == "add":
        return x + y
    elif operator == "multiply":
        return x * y
    else:
        raise ValueError("Only add and multiply supported.")

structured_calc_tool = StructuredTool.from_function(
    func=calculate,
    name="structured_calc",
    description="Use this tool to add or multiply two numbers. Provide 'x', 'y' and 'operator' ('add' or 'multiply')."
)
