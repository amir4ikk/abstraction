class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 5000

class Developer(Employee):
    def calculate_salary(self):
        return 3000

employee1 = Employee()
manager1 = Manager()
developer1 = Developer()

print("Salary for Employee:", employee1.calculate_salary())    # Output: No specific implementation for Employee class
print("Salary for Manager:", manager1.calculate_salary())      # Output: 5000
print("Salary for Developer:", developer1.calculate_salary())  # Output: 3000
