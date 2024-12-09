# Список для сортування
students = [
    {"name": "Anna", "grade": 90},
    {"name": "Andrey", "grade": 85},
    {"name": "Evgeniy", "grade": 92},
    {"name": "Roma", "grade": 88}
]

# Сортування за іменем
sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Сортування за іменем:")
for student in sorted_by_name:
    print(student)

# Сортування за оцінкою
sorted_by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\nСортування за оцінкою:")
for student in sorted_by_grade:
    print(student)
