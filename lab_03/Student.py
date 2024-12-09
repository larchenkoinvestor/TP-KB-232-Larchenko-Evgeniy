class Student:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def __str__(self):
        return f"Ім'я: {self.name}, Телефон: {self.phone}, Адреса: {self.address}, Електронна пошта: {self.email}"
