# 1. Create an array and add 5 numbers to it using append().

# nums = []
# for i in range(5):
#     nums.append(i)
# print(nums)

# 2. Find the length of the array and print the last item.

# nums = [1,2,3,4,5,6,7,8,9,0]
# print(len(nums))
# print(nums[-1])

# 3. Reverse the array using slicing.

# nums = [1,2,3,4,5,6,7,8,9,0]
# print(nums[::-1])

# 4. Count how many times a value appears.

# nums = [1,1,1,2,3,3,3,3,3,4,4,]
# print(nums.count(3))

# 5. Create a string

s = "Tushar"
# Convert it to uppercase
print(s.upper())

# Reverse it
rev = s[::-1]
print(rev)

# Check if it’s a palindrome
if rev == s:
    print("it's palindrome")
else:
    print("it's not palidronme")

# Count how many vowels it has
count=0
for ch in s:
    if ch.lower() in "aeiou":
        count+=1
print(count)

