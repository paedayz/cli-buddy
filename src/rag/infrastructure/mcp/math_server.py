# math_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    :params a: First number
    :params b: Second number
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers
    
    :prams a: First number
    :prams b: Second number
    """
    return a * b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers
    
    :prams a: First number
    :prams b: Second number
    """
    return a - b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """
    Divide two numbers
    
    :prams a: First number
    :prams b: Second number
    """
    return a / b

@mcp.tool()
def power(a: int, b: int) -> int:
    """
    Power two numbers
    
    :prams a: First number
    :prams b: Second number
    """
    return a ** b

@mcp.tool()
def sqrt(a: int) -> int:
    """
    Square root of a number
    
    :prams a: First number
    :prams b: Second number
    """
    return a ** 0.5

@mcp.tool()
def gcd(a: int, b: int) -> int:
    """
    GCD of two numbers
    
    :prams a: First number
    :prams b: Second number
    """
    return a if b == 0 else gcd(b, a % b)

@mcp.tool()
def lcm(a: int, b: int) -> int:
    """
    LCM of two numbers
    
    :prams a: First number
    :prams b: Second number
    """
    return a * b // gcd(a, b)

@mcp.tool()
def fibonacci(n: int) -> int:
    """
    Fibonacci of a number
    
    :params n: number of Fibonacci
    """
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    mcp.run(transport="stdio")