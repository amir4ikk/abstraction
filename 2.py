class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"

    def __add__(self, other):
        if isinstance(other, int):
            self.age += other
            return self
        else:
            print("Adding a student to a student is not allowed.")
            return 0


t1 = Student("John", 18, 12)
t2 = Student("Alice", 17, 11)

t1 += 5
print(t1)  

a = t1 + t2 
print(a)    