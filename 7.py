class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

vehicle1 = Vehicle()
car1 = Car()
motorcycle1 = Motorcycle()

print(vehicle1.start_engine())   
print(car1.start_engine())        
print(motorcycle1.start_engine())
