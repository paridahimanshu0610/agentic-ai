from mcp.server.fastmcp import FastMCP

my_mcp = FastMCP("MyFirstMCPServer")

@my_mcp.tool()
async def add(nums: list):
    """Add the input numbers

    Args:
        nums: List of numbers to add 
    """
    
    return sum(nums)

@my_mcp.tool()
async def subtract(a: int, b: int):
    """Subtract the input numbers

    Args:
        a: First integer argument
        b: Second integer argument 
    """

    return a-b

@my_mcp.tool()
async def multiply(a: int, b: int):
    """Add the input numbers

    Args:
        a: First integer argument
        b: Second integer argument 
    """

    return a*b

@my_mcp.tool()
async def divide(a: int, b: int):
    """Add the input numbers

    Args:
        a: First integer argument
        b: Second integer argument 
    """
    if b==0:
        raise ValueError("The denominator should not be zero")

    return a/b

if __name__ == "__main__":
    my_mcp.run(transport='stdio')