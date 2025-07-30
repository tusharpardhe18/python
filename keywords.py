# del keyword
'''
used to delete object properties or object itself

del s1.name
del s1

'''

# Private(like) attributes & methods
'''
conceptual implementation in python

private attributes & methods are meant to be used
only within the class and are not accessible from outside
the class
'''

class Account:
    def __init__(self, acc_no, acc_pass):
        self.account = acc_no
        self.__password = acc_pass
    
    def reset_pass(self):
        print(self.password)
    
acc = Account("123", "abc")

# print(acc.account)
# print(acc.__password)

# class Person:
#     __name = "anonymous"
    
#     def __hello(self):
#         print(f"hello, {self.__name}!!")
    
#     def welcome(self):
#         return self.__hello()
    
# a = Person()
# print(a.__name)
# print(a.__hello())
# a.welcome()


# Super Method
# super() method is ued to access methods of the parent class

class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotoCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

c = ToyotoCar("Fortuner", "Electric")
print(c.type)

# Class Method :
'''
a class method is bound to the class & receives the class as an implicit first argument

Note : static method can't access or modify class state &
generally for utility
'''

class Student:
    @classmethod # decorator
    def college(cls):
        pass

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Rahul"
    @classmethod
    def changeName(cls, name):
        cls.name = name

p = Person()
p.changeName("rahul")
print(p.name)
print(Person.name)

# static methods - @staticmethod
# class methods - @classmethod - (cls)
# instance methods - (self)

# Property (decorator)
# we use @property decorator on any method in the class
# to use the method as a property 

class Student1:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.math + self.chem + self.phy) / 3) + "%"

s1 = Student1(96,92,94)
print(s1.percentage) 

s1.phy = 100
print(s1.percentage)