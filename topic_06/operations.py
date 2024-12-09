import logging
from functions import add, subtract, multiply, divide

def input_num(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("Будь ласка, введіть коректне число.")

def execute_operation(command, a, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    try:
        if command in operations:
            result = operations[command](a, b)
            logging.debug(f"Виконано операцію {command}: {a} {command} {b} = {result}")
            return result
        else:
            raise ValueError("Невідома операція")
    except Exception as e:
        logging.error(f"Помилка при виконанні {command}: {e}")
        raise
