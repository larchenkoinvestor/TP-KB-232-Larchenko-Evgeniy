class ReversePolishNotation:
    def __init__(self):
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def is_operator(self, token):
        return token in self.operators

    def precedence(self, operator):
        return self.operators.get(operator, 0)

    def to_rpn(self, expression):
        output = []
        stack = []
        tokens = expression.split()
        parentheses_balance = 0  # Лічильник балансу дужок

        for token in tokens:
            if token.isnumeric() or token.replace('.', '', 1).isdigit():
                output.append(token)
            elif token == '(':
                stack.append(token)
                parentheses_balance += 1
            elif token == ')':
                parentheses_balance -= 1
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ValueError("Закриваюча дужка не має відповідної відкриваючої")
                stack.pop()  # Remove '('
            elif self.is_operator(token):
                while stack and self.is_operator(stack[-1]) and self.precedence(stack[-1]) >= self.precedence(token):
                    output.append(stack.pop())
                stack.append(token)
            else:
                raise ValueError(f"Некоректний токен у виразі: {token}")

        # Перевірка балансу дужок
        if parentheses_balance != 0:
            raise ValueError("Відкриваюча дужка не має відповідної закриваючої")

        while stack:
            if stack[-1] in '()':
                raise ValueError("Залишились невідповідні дужки у виразі")
            output.append(stack.pop())

        return output

    def evaluate_rpn(self, rpn_expression):
        stack = []

        for token in rpn_expression:
            if token.isnumeric() or token.replace('.', '', 1).isdigit():
                stack.append(float(token))
            elif self.is_operator(token):
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)

        return stack[0]

if __name__ == "__main__":
    try:
        expression = input("Введіть математичний вираз (наприклад, '3 + 4 * 2 / ( 1 - 5 ) ^ 2'): ")
        rpn_converter = ReversePolishNotation()

        # Конвертуємо у ЗПЗ
        rpn = rpn_converter.to_rpn(expression)
        print("Зворотний польський запис:", " ".join(rpn))

        # Обчислюємо результат
        result = rpn_converter.evaluate_rpn(rpn)
        print("Результат:", result)
    except ValueError as e:
        print("Помилка у виразі:", e)
    except IndexError:
        print("Помилка обчислення: можливо, вираз некоректний або недостатньо операндів.")
