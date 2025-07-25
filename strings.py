# string is a data type in python
# string is a sequence of characters enclosed in quotes
# we can primarily write a string in these three ways

a = 'harry'
b = "harry"
c = '''harry'''

# string slicing
# a string in python can be sliced for getting a part of the strings.

# consider the following string:

# the index in a strings from 0 to (length-1) in python. 
# in order to slice to string, we use the following syntax:

# sl = name[ind_start: ind_end]
# sl [0:3] returns "har" -> characters from 0 to 3
# sl [1:3] returns "ar" -> characters from 1 to 3

nameshort = a[1:3]
print(nameshort)

''' Negative Indices: Indices can also be used as shown int he figure above
-1 corresponds to the (length-1) index, -2 to (length-2)


# Escape Sequence Characters
Sequence of characters after backslash "\" - Escape Sequence Characters

Escape Sequence characters comprise of more than one character but 
represent one character when used within the strings.

example : \n, \t, \', \", \ etc.
 
 
 
 
'''