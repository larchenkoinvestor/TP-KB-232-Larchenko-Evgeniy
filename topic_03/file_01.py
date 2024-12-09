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

# Перевірка, чи введене число
def input_num(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():  # Перевірка числа з крапкою
            return float(value)
        print("Будь ласка, введіть коректне число.")

# Головна функція калькулятора
def main_calc():
    print("Калькулятор запущено! Введіть 'exit' для виходу.")
    while True:
        command = input("Введіть операцію (+, -, *, /) або 'exit': ").strip()
        if command.lower() == 'exit':
            print("Калькулятор завершено.")
            break
        
        if command not in ['+', '-', '*', '/']:
            print("Невідома операція.")
            continue
        
        a = input_num("Введіть перше число: ")
        b = input_num("Введіть друге число: ")
        
        if command == "+":
            print("Результат:", add(a, b))
        elif command == "-":
            print("Результат:", subtract(a, b))
        elif command == "*":
            print("Результат:", multiply(a, b))
        elif command == "/":
            print("Результат:", divide(a, b))

main_calc()
