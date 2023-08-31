## https://pynative.com/python-object-oriented-programming-oop-exercise/

# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(200, 300)
print(f"The modelX can go {modelX.max_speed} MPH and has a charge of {modelX.mileage} miles")


## OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicle:
    pass


# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

# Expected Output:

# Vehicle Name: School Volvo Speed: 180 Mileage: 12

class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)


# OOP Exercise 4: Class Inheritance
# Given:

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.
# Expected Output:

# The seating capacity of a bus is 50 passengers

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passangers"

class Bus(Vehicle):
    # assign default val to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


second_bus = Bus("School Volvo", 180, 12)
print(second_bus.seating_capacity())


# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.

class Vehicle:

    color = "white"

    def __init__(self,name, max_speed, mileage):
        
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus_3 = Bus("School Volvo", 180, 12)

personal_car = Car("Audi 05", 240, 18)

# Expected Output:

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

print(f"Color:", bus_3.color, "Vehicle name:", bus_3.name, "Speed:", bus_3.max_speed, "Mileage:", bus_3.mileage)
print(f"Color:", personal_car.color, "Vehicle name:", personal_car.name, "Speed:", personal_car.max_speed, "Mileage:", personal_car.mileage)