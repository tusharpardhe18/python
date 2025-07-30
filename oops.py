# Object Oriented Programming : 
'''
OOP is all about organizing code into objects 
(real-world entities), so your code becomes more 
reusable, modular, and easier to understand.

To map with real world  scenarios, 
we started using objects in code
 
This is called  object oriented programming
'''

# 1. Class and Object :
'''
- Class = Blueprint
-Object = Actual thing based on the blueprint

'''

# Defining a Class :

class Person:
    def __init__(self,fullname,myage):
        self.name = fullname
        self.age = myage
    
    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")

# Creating an Object :

p1 = Person("Tushar",22)
p1.greet()


# 2. __int__() Constructor :
'''
Runs automatically when you create an object. 
It's like a constructor in C++.
'''

def __init__(self, fullname):
    self.name = fullname


# 3. Instance vs Class Variables :

class Student:
    college = "IIT"  # Class variable
    name="anonymous"
    def __init__(self, fullname):
        self.name = fullname  # Instance variable

s = Student("karan")
print(s.name) # karan 
# instance var > class var


# 4. Instance Methods :
'''
Any method that uses self. Works on object-specific data.
'''
class Person:
    def __init__(self,fullname,myage):
        self.name = fullname
        self.age = myage
    
    # method
    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")
