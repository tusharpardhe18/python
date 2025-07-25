# Sets
'''
Collection of non-repetitive elements

s=set() -> no repetition allowed!!
s.add(1)
a.add(2) -> or set = {1,2}

if you are programming beginner without much knowloedge
of mathematical operations on sets, you can simply look 
at sets in python as datatypes conntaining unique values.

'''

s = {1,5,32,54,5,5,5}

print(s)

e = set()
# print(type(e))

# Properties
'''
- unordered
- unindexed
- there is no way to change items in sets
- sets can't contain duplicate values

'''

# Methods
'''
- s.add(5) : add element 5 if not alr there
- s.update([3,4,5]) : add multi elements
- s.remove(3) : remove 3 or raise error if missing
- s.discard(10) : Remove 10 if it exists, no error
- s.pop() : Remove and return a random element
- s.clear() : empty the set

- s.union(b) : all unique elements from both, s | b
- s.intersection(b) : elements common to both sets, s & b
- s.difference(b) : elements in s not in b, s - b
- s.symmetric_difference(b) : elements in s or b but not in both,  s ^ b

- s.issubset(b) : is a fully inside b
- s.issuperset(b) : does s contain b fully?
- s.isdisjoint(b) : no common elements at all?
'''
# s.add(10)
s.update([11,12,13])
print(s)
# s.remove(5)
# s.discard(1)
# s.pop()
# s.clear()

b = {100, 11, 12, 22, 220}

# print(s.union(b))
# print(s.intersection(b))
# print(s.difference(b))
# print(s.symmetric_difference(b))
c = {1,2,3,4}
d = {2,3,4}

print(c.issubset(d))
print(c.issuperset(d))
print(c.isdisjoint(d))

