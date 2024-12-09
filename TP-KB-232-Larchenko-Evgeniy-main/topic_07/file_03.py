class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        return "\n".join(self.history)

def main():
    calc = Calculator()

    while True:
        command = input("Введіть операцію (+, -, *, /) або 'exit' для виходу: ").strip()
        if command.lower() == "exit":
            print("Калькулятор завершено.")
            break

        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))

            if command == "+":
                print(f"Результат: {calc.add(a, b)}")
            elif command == "-":
                print(f"Результат: {calc.subtract(a, b)}")
            elif command == "*":
                print(f"Результат: {calc.multiply(a, b)}")
            elif command == "/":
                print(f"Результат: {calc.divide(a, b)}")
            else:
                print("Невідома операція.")
        except ZeroDivisionError as e:
            print(e)
        except ValueError:
            print("Будь ласка, введіть коректне число.")

        print("\nІсторія операцій:")
        print(calc.show_history())

if __name__ == "__main__":
    main()
