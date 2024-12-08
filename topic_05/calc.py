from operations import input_num, execute_operation

def main_calc():
    print("Калькулятор запущено! Введіть 'exit' для виходу.")
    
    while True:
        command = input("Введіть операцію (+, -, *, /) або 'exit': ").strip()
        if command.lower() == "exit":
            print("Калькулятор завершено.")
            break
        
        if command not in ["+", "-", "*", "/"]:
            print("Невідома операція. Спробуйте ще раз.")
            continue
        
        try:
            a = input_num("Введіть перше число: ")
            b = input_num("Введіть друге число: ")
            result = execute_operation(command, a, b)
            print(f"Результат: {result}")
        except ValueError:
            print("Будь ласка, введіть коректне число.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main_calc()
