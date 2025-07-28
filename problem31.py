# Create a list of squares of all odd numbers between 1 and 50.
# square = [x**2 for x in range(51) if x%2!=0]
# print(square)

# From a list of strings, create a list of only those with length > 5

# l1 = ["Tushar", "Aman", "Avish", "Shivam","Isha"]
# l2 = []

# for i in l1:
#     if len(i) <=5:
#         l2.append(i)
# print(l2)

# From a 2D list, create a new list that contains only even numbers.
# matrix = [[1, 2], [3, 4], [5, 6]]
# l = []
# for row in matrix:
#     for val in row:
#         if val%2==0:
#             l.append(val)
# print(l)

# Create a multiplication table of a number using list comprehension.
# num=int(input("Enter a number: "))
# table = [num*x for x in range(1,11)]
# print(table)

# Create a list of all numbers from 1 to 100 that are divisible by both 3 and 7
# l=[]
# for i in range(1,101):
#     if i%3==0 and i%7==0:
#         l.append(i)
# print(l)

# Given a sentence, create a list of all words that start with a vowel.
s="Python is the language of choice for many advanced data tasks for a very good reason.Python is one of the easiest advanced programming languages to learn. Intuitive structuresand semantics mean that for people who are not computer scientists, but maybe biologists,statisticians, or the directors of a start-up, Python is a straightforward way to perform a wide variety of data tasks. It is not just a scripting language, but a full-featured objectoriented programming language."
# s1=s.split()
# l=[word for word in s1 if word[0].lower() in "aeiou"]
# print(l)

# From a list of numbers, create a new list containing 'even' or 'odd' depending on the number.

# [1,2,3] → ['odd','even','odd']

l = [1,3,4,8,10,13,0]
l2=[]
for i in l:
    if i==0:
        l2.append("zero")
    elif i%2==0:
        l2.append("even")
    else:
        l2.append("odd")
print(l2)