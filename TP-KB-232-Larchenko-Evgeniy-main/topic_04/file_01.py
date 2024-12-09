# Функції для операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе.")
    return a / b

# Функція для введення числа
def input_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введене значення не є числом. Спробуйте ще раз.")
        except KeyboardInterrupt:
            print("\n Програму перервано користувачем.")
            exit(0)
        except EOFError:
            print("\n Завершено введення (EOF).")
            exit(0)

# Головна функція калькулятора
def main_calc():
    print("Калькулятор запущено! Введіть 'exit' для виходу.")
    
    while True:
        try:
            command = input("Введіть операцію (+, -, *, /) або 'exit': ").strip()
            if command.lower() == 'exit':
                print("Калькулятор завершено.")
                break

            if command not in ['+', '-', '*', '/']:
                print("Помилка: невідома операція. Спробуйте ще раз.")
                continue
            
            # Отримання чисел від користувача
            a = input_num("Введіть перше число: ")
            b = input_num("Введіть друге число: ")
            
            # Виконання операції
            if command == "+":
                print("Результат:", add(a, b))
            elif command == "-":
                print("Результат:", subtract(a, b))
            elif command == "*":
                print("Результат:", multiply(a, b))
            elif command == "/":
                try:
                    print("Результат:", divide(a, b))
                except ZeroDivisionError as e:
                    print(f"Помилка: {e}")
        
        except KeyboardInterrupt:
            print("\nПрограму перервано користувачем.")
            break
        except EOFError:
            print("\nЗавершено введення (EOF).")
            break

if __name__ == "__main__":
    main_calc()
