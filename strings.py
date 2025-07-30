# Strings : 
'''
- strings are also like arrays, just arrays of characters

s = "hello"
print(s[1]) # e

Key Things to Note:
- strings are immutable in python - you can't change them in place.
- so, modifying a string usually means creating a new string.

Common Operations :

Length  -  len(s)
Concatenation  -  s1 + s2
Slicing  -  s[1:4]
Reversing  -  s[::-1]
Changing case  -  s.upper(), s.lower()
Find substrings  -  'a' in s, s.find('lo')
Count Letters  -  s.count('l')


When to use Arrays vs Strings :

- use arrays(lists) when you're dealing with numbers or objects and need mutability

- use strings when you're working with text, patterns or sequences of characters

Summary :

- Arrays are mutbable but strings are not
- Both have O(1) time complexity while accessing them
- Arrays are modifiable but we have to create new string if we want to chnage it
- Array datatypes are numbers/objects and string datatypes are characters
'''