# print 10 to 1 using a for loop
# for i in range(10, 0, -1):
#     print(i)

# print all even numbers between 1 and 20 using a while loop

# i = 2
# while i<=20:
#     print(i)
#     i+=2

# count how many vowels are in a string using a for loop

# text = "tushar"
# v = 0
# vowel = "aeiouAEIOU"

# for char in text:
#     if char in vowel:
#         v+=1
# print(v)

# print the multiplication table of a number entered by the user.

# num = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{num} x {i} = {i*num}")

# print a triangle pattern of stars like this for n = 5
'''
*
**
***
****
*****
'''
# n = 5
# for i in range(1,n+1):
#     print("*"*i)

# sum of first n natural numbers using a for loop

# n = int(input("Enter a natural nummber: "))
# sum=0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# find the factorial of a number

# n = int(input("Enter a natural nummber: "))
# fact=1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

# Print all numbers divisible by 3 or 5 from 1 to 100

# n = 100
# for i in range(1,n+1):
#     if i%3==0 or i%5==0:
#         print(i)

# count and print how many digits are in a given number.

# num = int(input("Enter a number: "))
# count = 0

# if num == 0:
#     count = 1
# else:
#     while num!=0:
#         num = num//10
#         count+=1
# print(count)

# reverse a number

# n = int(input("number: "))
# rev = 0

# while n != 0:
#     digit = n % 10
#     rev = rev*10 + digit
#     n = n // 10
# print(rev)

# count how many uppercase and lowercase letters are in a given string

# w = "Hello"
# up = 0
# low = 0

# for char in w:
#     if char.isupper():
#         up+=1
#     elif char.islower():
#         low+=1
# print(f"Uppercase: {up}, Lowercase: {low}")

# print the index of each vowel in a given word

# w = "Hello"
# vowel = "aeiouAEIOU"
# print(w)
# for char in w:
#     if char in vowel:
#         print(f"Index of {char} is {w.index(char)}")

# remove all digits from a string
# input = "a1b2c3"
# output = "abc"

# s = "a1b2c3"
# num = "0123456789"
# output = ""

# for char in s:
#     if char not in num:
#         output += char
# print(output)

# create a new list containing the sqaure of all even numbers from a existing list

# l = [1,2,3,4,5,6,7,8,9,10]
# ls = []

# for i in l:
#     if i%2==0:
#         ls.append(i*i)

# print(ls)

# ask the user for 5 numbers and store them in a list using a loop, then print their avg

# l = []

# for i in range(5):
#     l.append(int(input("Enter a number: ")))

# avg = sum(l)/len(l)
# print(avg)

# print the pattern
# 1
# 12
# 123
# 1234

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="") # end="" prints on the same line
#     print() # for new line

# for n=5, print
# *****
# ****
# ***
# **
# *

# n=5
# for i in range(n,0,-1):
#     print("*"*i)

# Floyd’s Triangle (for n = 4):

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n=4
# num=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         num+=1
#         print(num,end=" ")
#     print()

# print 
#    *   
#   ***  
#  ***** 
# *******

# n=1
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))

# print
# *****
# *   *
# *   *
# *****

# rows = 4
# cols = 5

# for i in range(rows):
#     if i==0 or i==rows-1:
#         print("*"*cols)
#     else:
#         print("*"+" "*(cols-2)+"*")

# check if a number is palindrome or not(same forwards & backwards)

# n = int(input("Enter a number: "))
# value = n
# r = 0

# while n != 0:
#     digit = n%10
#     r = r*10 + digit
#     n = n // 10

# if value==r:
#     print("palindrome")
# else:
#     print("not a palindrome")

# check if a number is prime or not

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("not a prime")
# else:
#     for i in range(2, int(n*0.5)+1):
#         if n % i == 0:
#             print("not a prime")
#             break
#     print("prime")

# find the GCD (HCF) of two numbers using a loop.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b!=0:
#     a,b = b, a%b
# print("HCF is",a)

# fibonnaci series
# a = int(input("Enter number: "))
a=10
f=0
s=1
for i in range(0,a):
    if i<=1:
        next = i
    else:
        next = f+s
        f=s
        s=next
    print(next,end=" ")


