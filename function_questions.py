# Practice: Build Your Intuition

# Easy
# 1. Write a function to calculate the factorial of a number.

# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f *= i 
#     print(f)
# x = int(input("Enter a number: "))
# fact(x)


# 2. Write a function that returns the maximum of three numbers.

# def maximum(a,b,c):
#     m = max(a,b,c)
#     print(f"{m} is maximum") 

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
# maximum(a,b,c)

# 3. Write a function that checks if a string is a palindrome.

# def palindrome(x):
#     v=x
#     r=0
#     while x>0:
#         r=r*10+x%10
#         x//=10
#     if v==r:
#         print("palindrome")
#     else:
#         print("not a palindrome")
# palindrome(121)

# 4. Write a function that counts vowels in a string.

# def count_vowels(x):
#     count=0
#     for ch in x:
#         if ch.lower() in "aeiou":
#             count+=1
#     print(count)

# x=input("Enter a word: ")
# count_vowels(x)

# 5. Write a function to check if a number is prime.

# def is_prime(x):
#     if x<=1:
#         print("not a prime")
#     else:
#         for i in range(2, int(x*0.5)+1):
#             if x % i == 0:
#                 print("not a prime")
#                 break
#             print("prime")

# x = int(input("Enter a number: "))
# is_prime(x)

