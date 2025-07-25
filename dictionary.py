# Dictionary

'''
collection of keys-value pairs

Syntax: 
a = {
"key" : "value",
"harry" : "code",
"marks" : "100",
"list" : [1,2,9]
}

a["key"] # prints "value"
a[list] # prints [1,2,9]

'''

marks = {
    "tushar" : 100,
    "shub" : 56,
    "rohan" : 23
}

print(marks, type(marks))
print(marks["tushar"])

# Properties
'''
1. unordered
2. mutable
3. indexed
4. can't contain duplicate keys

'''

# Methods
'''
consider the following dictionary
a = {
"name" : "harry"
"from" : "india"
"marks" : [92,98,96]
}

- a.items() : returns a list of (key, value) tuples.
- a.keys() : returns a list of dict keys
- a.values() : return a list of dict values
- a.update({"friends":}) : update the dict with supplied key-value pairs
- a.get("name") : returns the value of the specified keys
- key in a : checks if key exists
- len(dict) : count of key-value pairs
- a[key] = val : add or update a value
- a.update(b) : merge/update values
- setdefault(key, default) : insert if key missing
- a.pop(key) : remove and return value by key
- a.popitem() : remove and return last item
- del a(key) : delete key-value pair
- a.clear() : remove all items

  more methods on docs.python.org
'''

print(marks.items())
print(marks.keys())
print(marks.values())


