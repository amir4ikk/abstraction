class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, course={self.course})"


students = [
    Student("John", 18, "Math"),
    Student("Alice", 17, "Science"),
    Student("Bob", 19, "English"),
    Student("Emily", 20, "Math"),
    Student("David", 18, "Science"),
    Student("Sarah", 19, "English")
]

sorted_students = sorted(students, key=lambda student: student.course)

for student in sorted_students:
    print(student)
