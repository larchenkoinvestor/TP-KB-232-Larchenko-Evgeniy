# Функції для операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ділення на нуль неможливе"
    return a / b

# Головна функція калькулятора
def calculator_match():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    oper = input("Введіть операцію (+, -, *, /): ")

    match oper:
        case "+":
            print("Результат:", add(a, b))
        case "-":
            print("Результат:", subtract(a, b))
        case "*":
            print("Результат:", multiply(a, b))
        case "/":
            print("Результат:", divide(a, b))
        case _:
            print("Невідома операція.")

calculator_match()
