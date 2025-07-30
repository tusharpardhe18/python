# Arrays :
'''
- collection of items stored in contigous memory locations
- in python, the closedt thing is a list
eg:
arr = [1,2,3,4]
'''
# Why Arrays ?
'''
- they let store mutliple values of the same type together
- you can access elements by index in O(1) time
'''

# Core Concepts :
'''
1. Indexing :
- directly access an element using its position
- starts from 0 in python

arr[0] - first element
arr[-1] - last element

2. Slicing :
- allow to grab a part of the array

arr[1:3] - aleemts at index 1 and 2
arr[::-1] - reverse a array

3. Mutation :
- lists in python are mutable, they can be changed

arr[2] = 99

4. Built-In Methods :

- most used ones
a. append(x)  -  add items tot he end
b. insert(i, x)  -  insert x at index i
c. pop()  -  remove last item
d. remove(x)  -  remove first occurrence of x
e. sort()  -  sort the list
f. reverse()  -  reverse the list in place
g. index(x)  -  return index of first occurrence
h. count(x)  -  count occurrence of x

'''