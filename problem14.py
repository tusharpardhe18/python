# accept marks of 6 students and display in sorted manner

marks = []

s1 = int(input("Enter marks of student 1: "))
marks.append(s1)
s2 = int(input("Enter marks of student 2: "))
marks.append(s2)
s3 = int(input("Enter marks of student 3: "))
marks.append(s3)
s4 = int(input("Enter marks of student 4: "))
marks.append(s4)
s5 = int(input("Enter marks of student 5: "))
marks.append(s5)
s6 = int(input("Enter marks of student 6: "))
marks.append(s6)

marks.sort()

print(marks)
