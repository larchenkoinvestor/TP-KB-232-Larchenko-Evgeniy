import unittest
from lab_02 import addNewElement, deleteElement, updateElement, students_list

class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        """Метод для налаштування початкових даних перед кожним тестом"""
        # Очищаємо список перед кожним тестом
        students_list.clear()

    def test_add_student(self):
        """Тест на додавання студента"""
        addNewElement('Alice', '0639876543', 'Kyiv', 'alice@example.com')
        self.assertEqual(len(students_list), 1)
        self.assertEqual(students_list[0]['name'], 'Alice')

    def test_delete_student(self):
        """Тест на видалення студента"""
        addNewElement('Bob', '0631234567', 'Lviv', 'bob@example.com')
        deleteElement('Bob')
        self.assertEqual(len(students_list), 0)

    def test_update_student(self):
        """Тест на оновлення інформації про студента"""
        addNewElement('Jon', '0630000000', 'Odesa', 'jon@example.com')
        updateElement('Jon', phone='0631111111', address='Kharkiv')
        self.assertEqual(students_list[0]['phone'], '0631111111')
        self.assertEqual(students_list[0]['address'], 'Kharkiv')

if __name__ == "__main__":
    unittest.main()
