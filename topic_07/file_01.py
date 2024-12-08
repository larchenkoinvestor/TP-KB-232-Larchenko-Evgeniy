class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

# Створення об'єкта класу Student
student1 = Student("Іван", 20)
student2 = Student("Марія", 22)


print(student1)  # Студент: Іван, Вік: 20
print(student2)  # Студент: Марія, Вік: 22
