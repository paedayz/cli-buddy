from src.rag.infrastructure.tools.math_tools import *
from src.rag.infrastructure.tools.google_work_space_tools import *
def execute_tool_call(call):
    
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
        "SetCalendar": lambda summary, start_time, end_time: setCalendar(summary, start_time, end_time),
        "SendMail": lambda to, subject, body: sendMail(to, subject, body),
    }
    return func_map[call['name']](**call['args'])