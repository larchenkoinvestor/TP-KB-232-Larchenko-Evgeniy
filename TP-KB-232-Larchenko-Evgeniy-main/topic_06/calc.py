import logging
from operations import input_num, execute_operation

# Налаштування логування
logging.basicConfig(
    filename="log.txt",                # Файл для збереження логів
    level=logging.INFO,                 # Рівень логування
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат записів
    datefmt="%Y-%m-%d %H:%M:%S"         # Формат дати
)

def main_calc():
    logging.info("Калькулятор запущено.")
    print("Калькулятор запущено! Введіть 'exit' для виходу.")
    
    while True:
        command = input("Введіть операцію (+, -, *, /) або 'exit': ").strip()
        if command.lower() == "exit":
            logging.info("Калькулятор end.")
            print("Калькулятор завершено.")
            break
        
        if command not in ["+", "-", "*", "/"]:
            logging.warning(f"Невідома операція: {command}")
            print("Невідома операція. Спробуйте ще раз.")
            continue
        
        try:
            a = input_num("Введіть перше число: ")
            b = input_num("Введіть друге число: ")
            result = execute_operation(command, a, b)
            logging.info(f"Операція: {a} {command} {b} = {result}")
            print(f"Результат: {result}")
        except ValueError:
            logging.error("Некоректне значення числа.")
            print("Будь ласка, введіть коректне число.")
        except ZeroDivisionError as e:
            logging.error(f"Помилка: {e}")
            print(e)


if __name__ == "__main__":
    main_calc()
