# Tuples
'''
Tuples in Python are immutable, so they don’t have as many methods as lists.
a = () -> empty table
a = (1, ) -> tuple with only one element needs a comma
a = (1,7,2) -> tuple with more than one element

'''

a = (1,4,5,3,3)
print(type(a))

# Tuple Methods
'''
Consider the following tuple.
a = (1,7,2)
- a.count(1) : a count(1) will return no of times 1 occurs in a

- a.index(1) will return the index of first occurence of 1 in a

- we can add to two tuples like print(t1+t2)

- we can slice by [1:4]

- we can unpack it 
- t1 = (1,2,3)
- a,b,c = t1
- print(a,b,c), it'll assign values to a, b & c.

- we can find an item which is already existing by using 'in' keyword
- print(1 in t1)

- we can find the length by len(t1)

- we can repeat the same tuple by t1*3

- we can find min() and max() in t1
'''

b = a.count(3)
print(b)

c = a.index(3)
print(c)