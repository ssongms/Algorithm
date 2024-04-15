N = int(input())
students = []

for i in range(N):
    stu = input()
    students.append(stu)
nameLen = len(students[0])

for i in range(nameLen-1, -1, -1):
    slicedStudents = []
    for stu in students:
        slicedStudents.append(stu[i:])
    if len(slicedStudents) == len(set(slicedStudents)):
        print(nameLen-i)
        break