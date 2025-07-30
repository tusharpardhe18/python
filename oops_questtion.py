# create student class that takes n ame & marks of 
# 3 subjects as argy=uments in constructor. 
# Then create a method to print the average.

class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.mark1 = sub1 
        self.mark2 = sub2 
        self.mark3 = sub3
    
    def avg(self):
        a = (self.mark1 + self.mark2 + self.mark3) / 3
        print(f"The average marks of {self.name} is {a}")

b = Student("Tushar", 61, 54, 37)
b.avg()

# Static Methods :
'''
Methods that don't use self parameter (work at class level)
'''
class Student:
    @staticmethod # decorator
    def college():
        print("LPU")

# decorators allow us to wrap another function in order to 
# extend the behaviour of the wrapped function, without 
# permanently modifying it
