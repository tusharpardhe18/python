# find out whether a student has passed or failed if
# it requires a total 40% and atleast 33% in each subject to pass
# assume 3 subjects and take marks as an input from the user

hin = int(input("Enter marks of hindi: "))
eng = int(input("Enter marks of english: "))
math = int(input("Enter marks of maths: "))

percentage = ((hin+eng+math) / 300)*100

if percentage>40 and hin>=33 and eng>=33 and math>=33:
    print("Passed", percentage)
else:
    print("Failed", percentage)
