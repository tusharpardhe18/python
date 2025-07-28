# Function :
'''
A function is a named block of code that performs a specific task. You define it once, and use (or "call") it as many times as needed.

Why Use Functions?

- Avoid repetition

- Make code readable and organized

- Test and debug smaller parts easily

- Separate logic from execution

Function Basics
'''
#  Defining a Function :

def greet():
    print("Hello!")

# Calling a Function :

greet() # Hello!

# Parameters and Arguments :

def greet(name):
    print(f"Hello, {name}!")

greet("Tushar") # Hello, Tushar!
# You can pass any types like numbers, strings, lists, other functions, etc.

# Return Values :

# Use return to send back data from a function.
def add(a, b):
    return a + b

result = add(3, 4)
print(result) # 7
# if you don’t use return, the function returns None by default.

# Default Parameters :

# you can set default values for parameters.
def greet(name="stranger"):
    print(f"Hello, {name}!")

greet()           # Hello, stranger!
greet("Alice")    # Hello, Alice!

# Variable Scope :

# local scope :
# variables declared inside a function exist only inside it
def f():
    x = 5  # local to f()
    print(x)

f() # 5
# print(x)   ❌ Error: x is not defined

# global scope :
# variables outside any function are global. You can access them inside functions, but to modify them, use global.

x = 10

def f():
    global x
    x = 20

f()
print(x) # 20
# avoid modifying globals—pass variables as arguments instead.

# Optional (But Powerful) Function Tools

# *args → Variable-length arguments
def add_all(*nums):
    return sum(nums)

print(add_all(1, 2, 3, 4))  # 10

# **kwargs → Variable-length keyword arguments
def profile(**info):
    for k, v in info.items():
        print(k, v)

profile(name="Tushar", age=22)


