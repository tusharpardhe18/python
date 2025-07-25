# create empty dict, allow 4 friends to enter their fav
# language as value and use key as their names. 
# Assume that the names are unique
dist = {}

name = input("Name: ")
lang = input("Fav language: ")
dist[name] = lang
name = input("Name: ")
lang = input("Fav language: ")
dist[name] = lang
name = input("Name: ")
lang = input("Fav language: ")
dist[name] = lang
name = input("Name: ")
lang = input("Fav language: ")
dist[name] = lang

print(dist)

# if the names of 2 friends are same name, what will happen
# only one of the friend's name printed

# if the names of 2 friends are same fav lang, what will happen
# both the friend's name got printed with same lang

