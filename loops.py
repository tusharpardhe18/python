# For Loops
'''
used for iterating over a sequence

for i in range(5):
    print(i)

what range(5) means: numbers from 0 to 4

also:

for ch in "hello":
    print(ch)
'''
# While Loop
'''
i = 0
while i < 5:
    print(i)
    i += 1
'''
# Loop control statements
'''
- break : exit the loop
- continue : skip current iteration
- else (rarely used but valid) : runs if the loop completes without hitting break

'''

for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Loop Finished")