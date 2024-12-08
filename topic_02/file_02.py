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
def calculator_if_else():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    oper = input("Введіть операцію (+, -, *, /): ")

    if oper == "+":
        print("Результат:", add(a, b))
    elif oper == "-":
        print("Результат:", subtract(a, b))
    elif oper == "*":
        print("Результат:", multiply(a, b))
    elif oper == "/":
        print("Результат:", divide(a, b))
    else:
        print("Невідома операція.")

calculator_if_else()
