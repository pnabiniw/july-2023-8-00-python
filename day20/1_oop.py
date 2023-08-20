# OOP stands for Object-Oriented Programming
# It is the way of the modeling the real world problems into a program
# It has two important components; Class and the Objects

# Classes are the blueprints of an object
# Objects are the instance of the class

# Major Features of Object-Oriented Programming
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction


class Vehicle:
    category = "car"  # This is a class attribute


v = Vehicle()  # This is creating an object of class Vehicle
print(v.category)  # car   # This is getting class attribute using an object
print(Vehicle.category)  # car  # This is getting class attribute using a class

v.category = "truck"
print(Vehicle.category)  # car
print(v.category)  # truck


class Vehicle:
    category = "car"  # class attribute

    def __init__(self, doors, color):  # this is a constructor
        self.doors = doors  # instance attribute
        self.color = color  # instance attribute

    def description(self):  # a method inside Vehicle class
        return f"Vehicle is {self.category}. Color is {self.color} and doors are {self.doors}"

    def change_color(self, color):  # this is also a method
        self.color = color


v1 = Vehicle(4, "red")
print(v1.category)  # car  # get_data
print(v1.doors)  # 4
print(v1.color)  # red

v1.category = "bike"  # set_data
print(Vehicle.category)  # car  # get_data
print(v1.category)  # bike  # get_data

v2 = Vehicle(2, "green")
print(v2.doors)  # 2
print(v2.color)  # green

print(v2.description())

v2.change_color("blue")
print(v2.color)  # blue


# function inside a class is called the method of that class and that can be called with the
# object of that class only

