class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

# Створення списку об'єктів Student
students = [
    Student("Іван", 20),
    Student("Марія", 22),
    Student("Анастасія", 19),
    Student("Олександр", 21)
]

# Сортування списку студентів за віком за допомогою lambda
sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованих студентів
for student in sorted_students:
    print(student)
