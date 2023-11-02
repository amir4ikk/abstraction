class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"


students = [
    Student("Nodirbek", 18, 12),
    Student("Nodirbek", 17, 11),
    Student("Nodirbek", 19, 12),
    Student("Nodirbek", 16, 10),
    Student("Nodirbek", 18, 11),
    Student("Nodirbek", 17, 10),
    Student("Nodirbek", 19, 12),
    Student("Nodirbek", 16, 10),
    Student("Nodirbek", 18, 11),
    Student("Nodirbek", 17, 11)
]

students.sort(key=lambda student: student.age)

for student in students:
    print(student)
