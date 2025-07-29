# Lambda Functions :
'''
Lambda functions are small, anonymous (no name) functions defined in a single line
use them when:
- need a quick function for a short task

- don't want to define a full def block
'''

# Syntax :
# lambda arguments: expression

'''
Examples :
1. Add two numbers :

add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

2. Square of a number :

num = lambda x: x**2
print(num(3))

3. Return the last character of a string

word = lambda x: x[-1]
print(word("Tushar"))

'''

# Lambda functions are limited to one expression. 
# You can't use statements like if, for, etc., unless they’re inside the expression.


# Built-in Functional Tools :

# 1. map() : applies a function to every item of an iterable (list, tuple, etc.)
'''
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]

same as

x=4
squared1 = []
for x in nums:
    squared1.append(x**2)
print(squared1)

'''

# 2. filter() : returns only items where the function returns True.

# nums = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4]

# 3. reduce() (from functools) : reduces a sequence into a single value by applying a function cumulatively.
'''
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

Here's how it works internally:

1 * 2 = 2

2 * 3 = 6

6 * 4 = 24

'''

# We can use these functions inside list comprehensions or higher level tasks

# Use lambda with sorted() :
'''
names = ['Alice', 'Bob', 'Zara']
sort = sorted(names, key=lambda x: x[-1])
print(sort)
'''
# Use map() with list comprehension (not common but doable)
'''
nums = [1,2,3]
n = [x for x in map(lambda x: x+10, nums)]
print(n)
'''

# combine filter() with list comprehension
'''
nums = [1,2,3,4,5]
n = [x for x in filter(lambda x: x>2, nums)]
print(n)
'''

# combine map() and filter()

nums = [1,2,3,4,5]
doubled_evens = list(map(lambda x: x*2, filter(lambda x: x%2 == 0, nums)))
print(doubled_evens)