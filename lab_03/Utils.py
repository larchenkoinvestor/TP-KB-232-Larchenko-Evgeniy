import csv
from Student import Student

class Utils:
    @staticmethod
    def load_from_file(filename):
        students = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(Student(row['name'], row['phone'], row['address'], row['email']))
            print(f"Дані завантажено з файлу {filename}.")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")
        return students

    @staticmethod
    def save_to_file(filename, students):
        try:
            with open(filename, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'address', 'email'])
                writer.writeheader()
                for student in students:
                    writer.writerow({'name': student.name, 'phone': student.phone, 'address': student.address, 'email': student.email})
            print(f"Дані успішно збережено у файл {filename}.")
        except Exception as e:
            print(f"Сталася помилка при збереженні даних: {e}")
