# find whether a given username contains less than 10 characters or not
u = input("enter a username: ")

if len(u) >= 10:
    print("valid username")
else:
    print("username required 10 characters")