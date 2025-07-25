# create a dict of hindi words with values as their english
# translation to input with an option to look it up!

dict = {
    "hi" : "namaste",
    "morning" : "subah",
    "evening" : "shaam",
    "word" : "shabd",
    "mango" : "aam"
}

print(dict.keys())
a = input("Enter the any english word from above list \nand get to know it's hindi trnaslation: ")

print(dict.get(a))