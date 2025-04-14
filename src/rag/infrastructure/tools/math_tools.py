from typing_extensions import Annotated, TypedDict

class Add(TypedDict):
    """Add two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]
    
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return f'{a} + {b} = {a + b}'


class Multiply(TypedDict):
    """Multiply two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]
    
def multiply(a: int, b: int) -> int:
    """Multiply two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return f'{a} * {b} = {a * b}'

class Subtract(TypedDict):
    """Subtract two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]

def subtract(a: int, b: int) -> int:
    """Subtract two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return f'{a} - {b} = {a - b}'

class Divide(TypedDict):
    """Divide two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]

def divide(a: int, b: int) -> int:
    """Divide two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return f'{a} / {b} = {a / b}'

class Power(TypedDict):
    """Power two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]
    
def power(a: int, b: int) -> int:
    """Power two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return f'{a} ^ {b} = {a ** b}'

class Sqrt(TypedDict):
    """Square root of an integer."""
    a: Annotated[int, ..., "First integer"]
    
def sqrt(a: int) -> int:
    """Square root of an integer.

    Args:
        a: First integer
    """
    return f'Square root of {a} = {a ** 0.5}'

class Factorial(TypedDict):
    """Factorial of an integer."""
    a: Annotated[int, ..., "First integer"]
    
def factorial(a: int) -> int:
    """Factorial of an integer.

    Args:
        a: First integer
    """
    return f'Factorial of {a} = {1 if a == 0 else a * factorial(a - 1)}'

class Fibonacci(TypedDict):
    """Fibonacci of an integer."""
    a: Annotated[int, ..., "First integer"]
    
def fibonacci(a: int) -> int:
    """Fibonacci of an integer.

    Args:
        a: First integer
    """
    return f'Fibonacci of {a} = {0 if a == 0 else 1 if a == 1 else fibonacci(a - 1) + fibonacci(a - 2)}'

class Prime(TypedDict):
    """Prime of an integer."""
    a: Annotated[int, ..., "First integer"]
    
def prime(a: int) -> int:
    """Prime of an integer.

    Args:
        a: First integer
    """
    return f'Prime of {a} = {True if a == 2 or (a % 2 != 0 and all(a % i != 0 for i in range(3, int(a ** 0.5) + 1, 2))) else False}'

class GCD(TypedDict):
    """GCD of two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]
    
def gcd(a: int, b: int) -> int:
    """GCD of two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return f'GCD of {a} and {b} = {a if b == 0 else gcd(b, a % b)}'

class LCM(TypedDict):
    """LCM of two integers."""
    a: Annotated[int, ..., "First integer"]
    b: Annotated[int, ..., "Second integer"]
    
def lcm(a: int, b: int) -> int:
    """LCM of two integers.

    Args:    
        a: First integer
        b: Second integer
    """
    return f'LCM of {a} and {b} = {a * b // gcd(a, b)}'

class Sum(TypedDict):
    """Sum of list of integers."""
    a: Annotated[list[int], ..., "List of integers"]
    
def sum(a: list[int]) -> int:
    """Sum of list of integers.

    Args:
        a: List of integers
    """
    return f'Sum of {a} = {sum(a)}'

class Mean(TypedDict):
    """Mean of list of integers."""
    a: Annotated[list[int], ..., "List of integers"]
    
def mean(a: list[int]) -> int:
    """Mean of list of integers.

    Args:
        a: List of integers
    """
    return f'Mean of {a} = {sum(a) / len(a)}'

class Median(TypedDict):
    """Median of list of integers."""
    a: Annotated[list[int], ..., "List of integers"]
    
def median(a: list[int]) -> int:
    """Median of list of integers.

    Args:
        a: List of integers
    """
    return f'Median of {a} = {sorted(a)[len(a) // 2]}'

class Mode(TypedDict):
    """Mode of list of integers."""
    a: Annotated[list[int], ..., "List of integers"]
    
def mode(a: list[int]) -> int:
    """Mode of list of integers.

    Args:
        a: List of integers
    """
    return f'Mode of {a} = {max(set(a), key=a.count)}'

class LetterCount(TypedDict):
    """Count alphabet in word or sentence"""
    a: Annotated[str, ..., "word or sentence"]
    b: Annotated[str, ..., "alphabet that want to count"]
    
def letter_counting(a: str, b: str) -> int:
    """Count letter in word or sentence

    Args:
        a: word or sentence
        b: alphabet that want to count
    """
    return f'There are {a.count(b)} {b} in {a}'

def execute_math_tool_call(call):
    
    func_map = {
        "Multiply": lambda a, b: multiply(a, b),
        "Add": lambda a, b: add(a, b),
        "LetterCount": lambda a, b: letter_counting(a, b),
        "Subtract": lambda a, b: subtract(a, b),
        "Divide": lambda a, b: divide(a, b),
        "Power": lambda a, b: power(a, b),
        "Factorial": lambda a: factorial(a),
        "Fibonacci": lambda a: fibonacci(a),
        "Prime": lambda a: prime(a),
        "GCD": lambda a, b: gcd(a, b),
        "LCM": lambda a, b: lcm(a, b),
        "Sum": lambda a: sum(a),
        "Mean": lambda a: mean(a),
        "Median": lambda a: median(a),
        "Mode": lambda a: mode(a),
        "Sqrt": lambda a: sqrt(a),
    }
    return func_map[call['name']](**call['args'])