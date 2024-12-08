from functions import add, subtract, multiply, divide
import logging

# Налаштування логування
logging.basicConfig(
    filename="calculator.log",           # Файл для збереження логів
    level=logging.INFO,                  # Рівень логування
    format="%(asctime)s - %(message)s",  # Формат записів
    datefmt="%Y-%m-%d %H:%M:%S"          # Формат дати
)

def input_num(prompt):

    return float(input(prompt))

def execute_operation(command, a, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    if command in operations:
        result = operations[command](a, b)
        log_action(command, a, b, result)
        return result
    else:
        raise ValueError("Невідома операція")

def log_action(command, a, b, result):
    
    logging.info(f"Операція: {a} {command} {b} = {result}")
