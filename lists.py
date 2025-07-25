# python lists are containers to store a set of values of any data type

# friends = ["apple", "akash", "rohan", 7, false]
# lists can store value of any datatype

# List Indexing

# A list can be indexed just like a string.

L1 = [7,9,"harry"]

L1[0] #7
L1[1] #9
# L1[70] #error
L1[0:2] #[7,9] -> list slicing 

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # unline strings, lists are mutable

print(friends[0])
print(friends[1:4])

# List Methods
'''
Consider the following list:
L1 = [1,8,7,2,21,15]

- L1.sort(): update the list to [1,2,7,8,15,21]
- L1.reverse(): updates the list to [15,21,2,7,8,1]
- L1.append(8): adds 8 at the end of the list
- L1.insert(3,8): this will add 8 at 3rd index
- L1.pop(2): will delete the element at index 2 and return its value
- L1.remove(21): this will remove 21 fromt he list

'''
friends.append("Tushar")
# print(friends)

friends.reverse()
# print(friends)

friends.insert(4,True)
# print(friends)

friends.pop(1)
# print(friends)

friends.remove("Aakash")
# print(friends)