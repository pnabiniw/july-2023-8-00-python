# Inheritance is the transfer of properties and methods to the child class
# from the parent class
# Types of inheritance in python
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

class Vehicle:   # Parent Class
    engine_type = "Petrol Engine"


class Bike(Vehicle):
    wheels = "two"


class Car(Vehicle):
    wheels = "four"


class Cycle(Bike):
    engine_type = None


car = Car()
print(car.engine_type)  # Petrol Engine
print(car.wheels)  # four


# Single Inheritance
class A:
    pass


class B(A):  # This is single inheritance
    pass


# Multiple Inheritance
class A:
    pass

class B:
    pass


class C(A, B):   # Multiple Inheritance
    pass


# Multilevel Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass


# Hierarchical Inheritance
class A:
    pass


class B(A):
    pass


class C(A):
    pass


# mro => mro stands for method resolution order. It is the order in which attributes in inheritance
# is searched

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass


e = E()
print(E.mro())

