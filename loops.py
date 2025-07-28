# For Loops
'''
used for iterating over a sequence

for i in range(5):
    print(i)

what range(5) means: numbers from 0 to 4

also:

for ch in "hello":
    print(ch)
'''
# While Loop
'''
i = 0
while i < 5:
    print(i)
    i += 1
'''
# Loop control statements
'''
- break : exit the loop
- continue : skip current iteration
- else (rarely used but valid) : runs if the loop completes without hitting break

'''

# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("Loop Finished")

# Nested loops
'''
a loop inside another loop

for i in range(1):
    for j in range(2):
        print(f"i={i}, j={j}")

# Common Use Cases:

- printing patterns (triangles, squares)

- traversing 2D arrays/lists

- working with string pairs, combinations

- basic matrix operations

# Built-in Functions/Tricks you'll Often Use:

- range(start, stop, step) : for counting in any direction.

- len() : to get the size of a string, list, etc.

end=" " : used in print() to stop newline for patterns.

ord() / chr() : convert between characters and ASCII.

enumerate() : gives you both index and value in a loop.

zip() : used to loop over two lists at once.

input().split() : handy to take multiple inputs at once.

int() / str() / list() : type conversions are often needed in nested logic.


'''
# Number Triangle
# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# multiplication from 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i*j:2}", end=" ")
#     print()

# 2D traversal
# matrix = [[1, 2], [3, 4], [5, 6]]
# for row in matrix:
#     for val in row:
#         print(val)


# List Comprehensions
'''
a shorter more readable way to create new lists from existing sequences

[expression for item in iterable if condition]

'''
# squares of numbers
squares = [x**2 for x in range(10)]
# print(squares)

#extract vowels
s="Hello World"
vowels = [ch for ch in s if ch.lower() in 'aeiou']
# print(vowels)

# only even numbers
evens = [x for x in range(20) if x % 2 == 0]
# print(evens)

# uppercase all words in a list
words = ['python', 'loops', 'comprehension']
uppercased = [word.upper() for word in words]
# print(uppercased)

# Common Functions Used with List Comprehensions
'''
- len()

- str(), int(), float()

- .upper(), .lower()

- .split(), .join()

- sum(), max(), min()
'''

