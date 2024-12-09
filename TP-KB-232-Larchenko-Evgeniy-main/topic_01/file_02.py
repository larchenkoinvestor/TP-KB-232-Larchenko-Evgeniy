# Тест функцій для роботи з рядками
def test_str_fun():
    test_str = input("Введіть рядок: ")

    print("strip():", test_str.strip())            # Видалення пробілів з боків
    print("capitalize():", test_str.capitalize())  # Перша літера з великої
    print("title():", test_str.title())            # Кожне слово з великої
    print("upper():", test_str.upper())            # Усі великі
    print("lower():", test_str.lower())            # Усі малі

test_str_fun()
