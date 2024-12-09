from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, name, phone, address, email):
        new_student = Student(name, phone, address, email)
        self.students.append(new_student)
        self.students.sort(key=lambda s: s.name)  # Відсортовано за іменем

    def delete_student(self, name):
        self.students = [student for student in self.students if student.name != name]

    def update_student(self, name, phone=None, address=None, email=None):
        for student in self.students:
            if student.name == name:
                if phone:
                    student.phone = phone
                if address:
                    student.address = address
                if email:
                    student.email = email
                return
        print("Студента з таким ім'ям не знайдено.")

    def print_all(self):
        if not self.students:
            print("Список студентів порожній.")
        else:
            for student in self.students:
                print(student)

    def get_students(self):
        return self.students
