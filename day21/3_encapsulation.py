# Encapsulation is the process of data hiding in OOP approach of programming.
# Using this feature we make our attributes private, public or/and protected

# Public Attributes
# These attributes are accessible from both inside the class and outside the class

class Vehicle:
    engine_type = "Petrol"  # Public member

    def description(self):
        return f"The vehicle has {self.engine_type} engine"


v = Vehicle()
print(v.engine_type)  # Petrol


# Protected Attributes
# These attributes should be accessible from the same class or the child class only

class Vehicle:
    _color = "blue"  # Protected member because of the single underscore in the beginning of the variable

    def color_desc(self):
        print(f"The color of the vehicle is {self._color}")


class Bike(Vehicle):
    def color_desc(self):
        print(f"The color of the bike is {self._color}")

b = Bike()
print(b._color)  # blue. Python is flexible. So it also allows the protected members to be accessible
                    # from outside the class. But, it is not recommended to do so.


# Private Attributes
class Vehicle:
    __color = "red"  # Private member because of the double underscore in the beginning of the variable

    def color_desc(self):
        return f"the color of the vehicle is {self.__color}"


v = Vehicle()
# print(v.__color)  # Attribute Error
print(v.color_desc())
