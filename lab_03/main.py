from StudentList import StudentList
from Utils import Utils

def main():
    student_list = StudentList()
    filename = "lab3.csv"

    # Завантаження даних
    student_list.students = Utils.load_from_file(filename)

    while True:
        choice = input("Оберіть дію [C створити, U оновити, D видалити, P роздрукувати, X вийти]: ").upper()
        if choice == "C":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            address = input("Адреса: ")
            email = input("Електронна пошта: ")
            student_list.add_student(name, phone, address, email)
        elif choice == "U":
            name = input("Ім'я: ")
            phone = input("Новий телефон (або залиште порожнім): ") or None
            address = input("Нова адреса (або залиште порожнім): ") or None
            email = input("Нова пошта (або залиште порожнім): ") or None
            student_list.update_student(name, phone, address, email)
        elif choice == "D":
            name = input("Ім'я студента для видалення: ")
            student_list.delete_student(name)
        elif choice == "P":
            student_list.print_all()
        elif choice == "X":
            Utils.save_to_file(filename, student_list.get_students())
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
