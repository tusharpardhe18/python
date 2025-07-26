# calulate the grade of a student from his marks from the following scheme:
'''
100-90 => O
90-80 => A
80-70 => B
70-60 => C
60-50 => D
<50 => F
'''

m = int(input("Enter your marks out of 100: "))

if m>=90:
    print("O grade")
elif m>=80:
    print("A grade")
elif m>=70:
    print("B grade")
elif m>=60:
    print("C grade")
elif m>=50:
    print("D grade")
elif m<50:
    print("F grade")
else:
    print("Invalid marks")
