import logging

def add(a, b):
    result = a + b
    logging.debug(f"Виконується додавання: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.debug(f"Виконується віднімання: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.debug(f"Виконується множення: {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        logging.error("Спроба ділення на нуль.")
        raise ZeroDivisionError("Ділення на нуль неможливе.")
    result = a / b
    logging.debug(f"Виконується ділення: {a} / {b} = {result}")
    return result
