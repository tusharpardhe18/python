#                        OOPS
#      ___________________|______________________
#     |            |              |              |
# Abstraction  Encapsulation  Inheritance  Polymorphism

'''
1. Abstraction :
- hiding the implementation details of a class and 
- only showing the essential features to the user.
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clucth = False
    
    def start(self):
        self.acc = True
        self.clucth = True
        print("car started...")

c = Car()
c.start()


'''
2. Encapsulation :
- wrapping data and functions into a single unit(object)
- hiding internal data and using methods to interact with it.
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# access private with name mangling :

# acc._BankAccount__balance

'''
3. Inheritance :
- child class inherits properties/methods of parent class.
'''
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")


'''
4. Polymorphism :
- same method name, different behavior.
'''
animals = [Dog(), Animal()]
for a in animals:
    a.sound()  # Polymorphism
