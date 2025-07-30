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

# define a Circle class to create a circl with radius r using the constructor
# define an Area() method of the class which calculates the area of the circle
# define a perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:
    def __init__(self, r):
        self.radius = r 
    
    def area(self):
        return (22/7) * self.radius**2

    def perimeter(self):
        return (22/7) * self.radius * 2

c = Circle(4)
print(c.area())
print(c.perimeter())


# define a Employee class with attributes role, department & salary. this class also has a showDetails() method. Create a Engineer class that inherits properties from Employee & has additional attributes : name & age

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"Role is {self.role}")
        print("Department is", self.dept)
        print("Salary is Rs.", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Developer", "Corporate", 50000)

engg = Engineer("Tushar", 22)
engg.showDetails()


# Create a class Order which stores item & its price.
# Use dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order 2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("chips", 20)
order2 = Order("drink", 15)

print(order1 > order2)
