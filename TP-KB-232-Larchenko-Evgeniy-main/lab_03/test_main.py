import unittest
from StudentList import StudentList
from Student import Student
from Utils import Utils
filename = "lab3(test).csv"

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        self.student_list.add_student("Alice", "123456789", "Kyiv", "alice@example.com")
        self.assertEqual(len(self.student_list.get_students()), 1)
        self.assertEqual(self.student_list.get_students()[0].name, "Alice")

    def test_delete_student(self):
        self.student_list.add_student("Bob", "987654321", "Lviv", "bob@example.com")
        self.student_list.delete_student("Bob")
        self.assertEqual(len(self.student_list.get_students()), 0)

    def test_update_student(self):
        self.student_list.add_student("Jon", "000000000", "Odesa", "jon@example.com")
        self.student_list.update_student("Jon", phone="111111111", address="Kharkiv")
        student = self.student_list.get_students()[0]
        self.assertEqual(student.phone, "111111111")
        self.assertEqual(student.address, "Kharkiv")
    
    # Додавання кількох студентів для тесту
    def test_add_multiple_students(self):
        self.student_list.add_student("Alice", "123456789", "Kyiv", "alice@example.com")
        self.student_list.add_student("Bob", "987654321", "Lviv", "bob@example.com")
        self.assertEqual(len(self.student_list.get_students()), 2)


    def tearDown(self):
        print("Тест завершено, збереження даних...")
        students = self.student_list.get_students()
        print(f"Кількість студентів для збереження: {len(students)}")
        Utils.save_to_file(
            r"E:\Cp and labs\TP-KB-232-Larchenko-Evgeniy\lab_03\lab3(test).csv",
            students
        )

if __name__ == "__main__":
    unittest.main()

