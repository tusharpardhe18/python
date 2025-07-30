# File Handling :
# 1. Opening a File

f = open("file.txt", "r")  # 'r' = read mode

# 2. Modes:
'''
# "r" - Read (default)

# "w" - Write (creates new or overwrites)

# "a" - Append

# "x" - Create (error if file exists)

# "b" - Binary (like images)

# "t" - Text mode (default)
'''

# 3. Reading a File :

f = open("file.txt", "r")
content = f.read()             # Reads entire file
lines = f.readlines()          # Returns list of lines
line = f.readline()            # Reads one line
f.close()

# 4. Writing to a File :

f = open("file.txt", "w")
f.write("Hello World\n")
f.writelines(["Line 1\n", "Line 2\n"])
f.close()

# 4. Best Practice: Use with (auto-closes file) :

with open("file.txt", "r") as f:
    data = f.read()

# Error Handling (Exceptions) :
# Python will crash on runtime errors unless you handle them.

# 1. Basic Try-Except :

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Invalid number.")


# 2. Catch All Errors :

try:
    risky_code()
except Exception as e:
    print("Something went wrong:", e)

# 3. else and finally :

try:
    print("Trying...")
except:
    print("Error!")
else:
    print("No error!")
finally:
    print("Always runs")


#  Modules and Packages :
#  What’s a Module?
# A module is just a .py file containing functions, classes, variables you can reuse.

# Example:

# utils.py
def add(a, b):
    return a + b

# main.py
import utils
print(utils.add(3, 4))

# 1. Import Styles

import math
from math import sqrt, pi
import random as rnd

# 2. Built-in Modules to Explore
'''
# math – square root, sin, log, etc.

# random – generate random numbers

# datetime – work with dates and time

# os – file system access

# sys – command line args, system functions

'''

# 3. Create a Package

# Folder structure:

# mypackage/
# ├── __init__.py
# ├── file1.py
# └── file2.py

# Then use:

from mypackage import file1