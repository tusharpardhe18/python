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
# c.start()


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
- when one class(child/derived) derives the properties & 
methods of another class(parent/base)
'''

class Car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

# print(car1.name)
# car1.start()


# Types :
'''
a. Single :
- one child class inherits from one parent class.

class A -> class B

'''
class Animal:
    def speak(self):
        print("animal speaks")
    
class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
# d.speak()
# d.bark()

'''
b. Multiple :
- one child class inherits from more than one parent class

class A, class B -> class C
'''
# multiple parent class
class Father:
    def skills(self):
        print("Gardening, Programming")
class Mother:
    def hobbies(self):
        print("Cookink, Painting")

# child class
class Child(Father, Mother):
    def own(self):
        print("Gaming")

c = Child()
# c.skills()
# c.hobbies()
# c.own()

'''
- if both parent classes have a method with the same name,
Python follows Method Resolution Order (MRO) 
— it picks the one from the first parent listed in the 
parentheses.

c. Multi-Level :
- class inherits from a child class, which itself inherited 
from a parent

class A -> clas B -> class C
'''
class Grandparent:
    def home(self):
        print("Own a house")

class Parent(Grandparent):
    def car(self):
        print("Own a car")

class Child(Parent):
    def laptop(self):
        print("own a Laptop")

c = Child()
# c.home()
# c.car()
# c.laptop()

'''
d. Hierarchical :
- multiple child classes inherit from the same parent.

class A -> class B and class A -> class C
'''
class Parent:
    def say_hi(self):
        print("Hi from Parent")

class Child1(Parent):
    def msg1(self):
        print("Child 1 here")

class Child2(Parent):
    def msg2(self):
        print("Child 2 here")

c1 = Child1()
c2 = Child2()
# c1.say_hi()
# c2.say_hi()

'''
e. Hybrid :
- mix of two or more types (like multiple + multilevel).
Python handles hybrid inheritance using MRO 
(Method Resolution Order) internally, especially 
when there's ambiguity.

multiple + multilevel
'''
class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    pass

class D(B, C):
    pass

d = D()
# d.method()  # Follows MRO: D → B → C → A


'''
4. Polymorphism : Operator Overloading
- same method name, different behavior.
- when the operator is allowed to have different meaning 
according to the context

Operators & Dunder functions :
a+b #addition     a.__add__(b)
a-b #subtraction  a.__sub__(b)
a*b #multiplition a.__mul____(b)
a/b #division     a.__turediv____(b)
a%b #mod          a.__mod____(b)
'''

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()

num = num1-num2
num.showNumber()