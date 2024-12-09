import unittest
from lab_02 import addNewElement, deleteElement, updateElement, students_list ,save_data_to_csv

class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        # Очищаємо список перед кожним тестом
        students_list.clear()

    def test_add_student(self):
        addNewElement('Alice', '0639876543', 'Kyiv', 'alice@example.com')
        self.assertEqual(len(students_list), 1)
        self.assertEqual(students_list[0]['name'], 'Alice')

    def test_delete_student(self):
        addNewElement('Bob', '0631234567', 'Lviv', 'bob@example.com')
        deleteElement('Bob')
        self.assertEqual(len(students_list), 0)

    def test_update_student(self):
        addNewElement('Jon', '0630000000', 'Odesa', 'jon@example.com')
        updateElement('Jon', phone='0631111111', address='Kharkiv')
        self.assertEqual(students_list[0]['phone'], '0631111111')
        self.assertEqual(students_list[0]['address'], 'Kharkiv')

    def tearDown(self):
        save_data_to_csv(r"E:\Cp and labs\TP-KB-232-Larchenko-Evgeniy\lab_02\lab2(test).csv")


if __name__ == "__main__":
    unittest.main()
