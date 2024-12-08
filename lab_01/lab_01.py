students_list = [
    {"name": "Bob", "phone": "0631234567", "address": "Kyiv", "email": "bob@example.com"},
    {"name": "Emma", "phone": "0631234567", "address": "Lviv", "email": "emma@example.com"},
    {"name": "Jon", "phone": "0631234567", "address": "Odesa", "email": "jon@example.com"},
    {"name": "Zak", "phone": "0631234567", "address": "Kharkiv", "email": "zak@example.com"}
]

def printAllList():
    for elem in students_list:
        strForPrint = f"Ім'я: {elem['name']}, Телефон: {elem['phone']}, Адреса: {elem['address']}, Електронна пошта: {elem['email']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Будь ласка, введіть ім'я студента: ")
    phone = input("Будь ласка, введіть телефон студента: ")
    address = input("Будь ласка, введіть адресу студента: ")
    email = input("Будь ласка, введіть електронну пошту студента: ")
    
    # Створюємо новий запис
    newItem = {"name": name, "phone": phone, "address": address, "email": email}
    
    # Знаходимо правильну позицію для вставки, щоб список залишався відсортованим за іменем
    insertPosition = 0
    for item in students_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students_list.insert(insertPosition, newItem)
    print("Новий елемент був доданий")
    return

def deleteElement():
    name = input("Будь ласка, введіть ім'я студента, якого потрібно видалити: ")
    deletePosition = -1
    for item in students_list:
        if name == item["name"]:
            deletePosition = students_list.index(item)
            break
    if deletePosition == -1:
        print("Елемент не знайдений")
    else:
        print(f"Студента знайдено на позиції {deletePosition}")
        del students_list[deletePosition]
    return

def updateElement():
    name = input("Будь ласка, введіть ім'я студента, якого потрібно оновити: ")
    updatePosition = -1
    for index, item in enumerate(students_list):
        if item["name"] == name:
            updatePosition = index
            break
    
    if updatePosition == -1:
        print("Студент не знайдений")
        return
    
    # Виводимо поточну інформацію про студента
    print(f"Поточна інформація: Ім'я: {students_list[updatePosition]['name']}, "
          f"Телефон: {students_list[updatePosition]['phone']}, "
          f"Адреса: {students_list[updatePosition]['address']}, "
          f"Електронна пошта: {students_list[updatePosition]['email']}")
    
    # Запитуємо нову інформацію
    phone = input("Будь ласка, введіть новий телефон: ")
    address = input("Будь ласка, введіть нову адресу: ")
    email = input("Будь ласка, введіть нову електронну пошту: ")

    # Оновлюємо дані
    students_list[updatePosition]["phone"] = phone
    students_list[updatePosition]["address"] = address
    students_list[updatePosition]["email"] = email
    print(f"Дані студента {name} оновлені.")
    return

def main():
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
                break
            case _:
                print("Неправильний вибір")

if __name__ == "__main__":
    main()
