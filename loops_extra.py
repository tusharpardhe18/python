# Advanced Loops & Comprehension Tricks
'''
1. enumerate(): Get Index + Value in Loops
- Why it’s useful:
If you're looping through a list and need both the value and its index, 
enumerate() is cleaner than manually using a counter.
'''

fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

for i, val in enumerate(fruits, start=1):
    print(f"{i}. {val}")


