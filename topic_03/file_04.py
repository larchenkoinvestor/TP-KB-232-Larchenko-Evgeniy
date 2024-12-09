# Функція для пошуку позиції вставки нового елементу у відсортованому списку
def find_ins_pos(sorted_list, element):

    # Проходимо по списку за допомогою індексу
    for i in range(len(sorted_list)):
        # Якщо елемент менший або дорівнює поточному значенню, повертаємо індекс
        if element <= sorted_list[i]:
            return i
    # Якщо елемент більший за всі значення у списку, вставляємо його в кінець
    return len(sorted_list)

# Головна програма для тестування
print("Введіть відсортований список чисел, розділених пробілами:")
sorted_list = list(map(int, input().split()))  # Перетворюємо введений текст на список чисел
print("Введіть число, яке потрібно вставити:")
element = int(input())  # Число для вставки

# Викликаємо функцію для знаходження позиції
position = find_ins_pos(sorted_list, element)

# Виводимо результат
print(f"Число {element} потрібно вставити на позицію {position}.")
print(f"Новий список: {sorted_list[:position] + [element] + sorted_list[position:]}")
