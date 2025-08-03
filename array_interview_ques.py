# 1. Find the maximum value in an array
'''
Problem:
Given an array of integers, find and return the maximum element.

Example:
Input: [3, 17, 4, 12] → Output: 17
'''

def max(arr):
    if not arr:
        return None

    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

arr = [3,17,4,12,67]
print(max(arr))


# 2. Reverse the array (in-place)
'''
Problem:
Given an array, reverse its elements without using extra space.

Example:
Input: [1, 2, 3, 4] → Output: [4, 3, 2, 1]
'''

def reverser_in_place(arr2):
    left = 0
    right = len(arr2) - 1

    while left < right:
        #swap
        arr2[left], arr2[right] = arr2[right], arr2[left]
        #move pointer
        left += 1 
        right -= 1
    return arr2

arr2 = [1, 2, 3, 4]
print(reverser_in_place(arr2)) 


# 3. Check if an array is sorted (ascending order)
'''
Problem:
Return True if the array is sorted in increasing order, else return False.

Example:
Input: [2, 4, 7, 9] → Output: True
Input: [5, 3, 8] → Output: False
'''

def is_sorted(arr3):
    if len(arr) == 1 or 0:
        return True

    for i in range(len(arr3)-1):
        if arr3[i] > arr3[i+1]:
            return False
    return True

arr3 = [1,2,2]
print(is_sorted(arr3)) 

# 4. Find the second largest element
'''
Problem:
Given an array, return the second-largest distinct element.

Example:
Input: [10, 5, 20, 20] → Output: 10
'''

def second_largest(arr4):
    largest = -1
    sec_large = -1
    for i in range(len(arr4)):
        if arr4[i] > largest:
            largest = arr4[i]

    for i in range(len(arr4)):
        if arr4[i] > sec_large and arr4[i] != largest:
            sec_large = arr4[i]
    return sec_large

arr4 = [10, 5, 25, 20]
print(second_largest(arr4))

# 5. Move all zeroes to the end
'''
Problem:
Given an array, move all 0s to the end while maintaining the 
order of non-zero elements.

Example:
Input: [0, 1, 0, 3, 12] → Output: [1, 3, 12, 0, 0]
'''

def move_zeroes(arr5):
    non_zero_index = 0

    # First pass: move non-zero elements to the front
    for i in range(len(arr5)):
        if arr5[i] != 0:
            arr5[non_zero_index] = arr5[i]
            non_zero_index += 1

    # Second pass: fill the remaining with zeroes
    for i in range(non_zero_index, len(arr5)):
        arr5[i] = 0

    return arr5

arr5 = [0, 1, 0, 3, 12]
print(move_zeroes(arr5))

# 6. Rotate array by one
'''
Problem:
Rotate the elements to the right by one place.

Example:
Input: [1, 2, 3, 4] → Output: [4, 1, 2, 3]
'''

def rotate_byOne(a6):
    last = a6[-1]
    for i in range(len(a6)-1,0,-1):
        a6[i] = a6[i-1]
    a6[0] = last
    return a6

a6 = [1, 2, 3, 0]
print(rotate_byOne(a6))


# 7. Count the number of even and odd elements
'''
Problem:
Return the number of even and odd numbers in an array.

Example:
Input: [1, 2, 3, 4, 5] → Output: Even: 2, Odd: 3
'''

def evenAndOdd(e):
    even = 0
    odd = 0
    for i in range(len(e)):
        if e[i]%2==0:
            even += 1
        else:
            odd += 1        
    print("Even:", even, "Odd:", odd)

e = [1,2,3,4,5]
evenAndOdd(e)


# 8. Find duplicates in an array
'''
Problem:
Return a list of duplicates from the array.

Example:
Input: [1, 3, 4, 2, 3, 1] → Output: [3, 1]
'''

def duplicates(d):
    dupli=[]
    for i in range(len(d)):
        for j in range(i+1,len(d),1):
            if d[i] == d[j] and d[i] not in dupli:
                dupli.append(d[i])
    return dupli

d = [1,3,4,2,3,3,1]
print(duplicates(d))


# 9. Return the sum of all elements
'''
Problem:
Just add up all the values in the array.

Example:
Input: [4, 5, 6] → Output: 15
'''

def sumAll(s):
    sum = 0
    for i in range(len(s)):
        sum += s[i]
    return sum

s = [4,5,6]
print(sum(s))


# 10. Find the missing number in 1 to n
'''
Problem:
Given n-1 elements from the range 1 to n, find the missing number.

Example:
Input: [1, 2, 4, 5] (n=5) → Output: 3
'''

def findMissingNo(f):
    sumOfN= n * (n+1) // 2
    sumOfArray = 0
    Diff = 0
    for i in range(len(f)):
        sumOfArray += f[i]
        Diff = sumOfN - sumOfArray
    return Diff

f=[1,2,4,5]
n=int(input("enter range: "))
print(findMissingNo(f))

# Left & Right Array Rotation

arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 3
i=0
#rotate left
arr[k:] = arr[k:][::-1]
arr[i:] = arr[i:][::-1]
arr[n-k:] = arr[n-k:][::-1]
print(arr)

#rotate right
# arr[n-k:] = arr[n-k:][::-1]
# arr[i:] = arr[i:][::-1]
# arr[k:] = arr[k:][::-1]
