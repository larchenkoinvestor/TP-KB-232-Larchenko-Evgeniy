import csv
import sys

# Ініціалізований вже відсортований список студентів
students_list = []

def load_data_from_csv(lab2):
    global students_list
    try:
        with open(lab2, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_list = [row for row in reader]
        print(f"Дані завантажено з файлу {lab2}")
    except FileNotFoundError:
        print(f"Файл {lab2} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при завантаженні даних: {e}")

def save_data_to_csv(lab2):
    try:
        with open(lab2, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'phone', 'address', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students_list)
        print(f"Дані успішно збережено в файл {lab2}")
    except Exception as e:
        print(f"Сталася помилка при збереженні даних: {e}")


def printAllList():
    if not students_list:
        print("Список студентів порожній.")
        return
    for elem in students_list:
        strForPrint = f"Ім'я: {elem['name']}, Телефон: {elem['phone']}, Адреса: {elem['address']}, Електронна пошта: {elem['email']}"
        print(strForPrint)
    return

def addNewElement(name=None, phone=None, address=None, email=None):
    if name is None:
        name = input("Будь ласка, введіть ім'я студента: ")
    if phone is None:
        phone = input("Будь ласка, введіть телефон студента: ")
    if address is None:
        address = input("Будь ласка, введіть адресу студента: ")
    if email is None:
        email = input("Будь ласка, введіть електронну пошту студента: ")
    
    newItem = {"name": name, "phone": phone, "address": address, "email": email}
    
    # Insert in sorted order
    insertPosition = 0
    for item in students_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students_list.insert(insertPosition, newItem)
    print("Новий елемент був доданий")
    return

def deleteElement(name=None):
    if name is None:
        name = input("Будь ласка, введіть ім'я студента, якого потрібно видалити: ")
    
    deletePosition = -1
    for item in students_list:
        if name == item["name"]:
            deletePosition = students_list.index(item)
            break
    if deletePosition == -1:
        print("Елемент не знайдений")
    else:
        del students_list[deletePosition]
        print(f"Студента '{name}' видалено.")
    return

def updateElement(name=None, phone=None, address=None, email=None):
    if name is None:
        name = input("Будь ласка, введіть ім'я студента, якого потрібно оновити: ")
    
    updatePosition = -1
    for index, item in enumerate(students_list):
        if item["name"] == name:
            updatePosition = index
            break
    
    if updatePosition == -1:
        print("Студент не знайдений")
        return
    
    # Update fields if provided, otherwise ask for input
    students_list[updatePosition]["phone"] = phone or input("Будь ласка, введіть новий телефон: ")
    students_list[updatePosition]["address"] = address or input("Будь ласка, введіть нову адресу: ")
    students_list[updatePosition]["email"] = email or input("Будь ласка, введіть нову електронну пошту: ")
    print(f"Дані студента {name} оновлені.")
    return


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть файл для завантаження даних.")
        return
    
    # Завантаження даних із CSV файлу
    load_data_from_csv(sys.argv[1])

    while True:
        choice = input("Будь ласка, виберіть дію [C створити, U оновити, D видалити, P роздрукувати, X вийти]: ")
        match choice:
            case "C" | "c":
                print("Створення нового елемента:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Оновлення існуючого елемента")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Елемент буде видалений")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("Список буде роздрукований")
                printAllList()
            case "X" | "x":
                print("Вихід з програми.")
                save_data_to_csv(sys.argv[1])  # Збереження даних у файл перед виходом
                break
            case _:
                print("Неправильний вибір")

if __name__ == "__main__":
    main()
