from functions import add, subtract, multiply, divide

def input_num(prompt):
    
    return float(input(prompt))

def execute_operation(command, a, b):
    if command == "+":
        return add(a, b)
    elif command == "-":
        return subtract(a, b)
    elif command == "*":
        return multiply(a, b)
    elif command == "/":
        return divide(a, b)
