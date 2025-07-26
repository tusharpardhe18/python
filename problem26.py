# detect spam comment

a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

comment = input("Enter a comment: ")

if a in comment or b in comment or c in comment or d in comment:
    print("Spam Detected")
else:
    print("No spam comments")