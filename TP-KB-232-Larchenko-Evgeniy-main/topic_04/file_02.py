# Функції для операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # Функція повертає результат ділення, виняток обробляється у main_calc

# Функція для введення чисел
def input_num(prompt):
    return float(input(prompt))  # Прямий виклик без перевірки

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
        
        # Введення чисел
        a = input_num("Введіть перше число: ")
        b = input_num("Введіть друге число: ")
        
        # Виконання операції
        try:
            if command == "+":
                print("Результат:", add(a, b))
            elif command == "-":
                print("Результат:", subtract(a, b))
            elif command == "*":
                print("Результат:", multiply(a, b))
            elif command == "/":
                print("Результат:", divide(a, b))
        except ZeroDivisionError:
            print("Помилка: спроба поділити на нуль.")

if __name__ == "__main__":
    main_calc()
