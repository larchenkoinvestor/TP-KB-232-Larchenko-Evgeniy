# Реверс рядка через введення
def reverse_str():
    s = input("Введіть рядок: ")  # Користувач вводить рядок
    rev_str = s[::-1]             # Реверс рядка
    print("Реверс:", rev_str)     # Виведення результату

reverse_str()