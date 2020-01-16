"""HACKERRANK PROGRAM
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""


if __name__ == '__main__':
    a=[]
    b=[]
    low=0
    c=0
    d=[]
    for _ in range(int(input("enter number of students"))):
        name = input("enter name")
        score = float(input("enter score"))
        a.append([name,score])

    for i in range(len(a)):
        b.append(a[i][1])
    b.sort()
    low=b[0]
    for j in range(1,len(b)):
        if low != b[j]:
            c=b[j]
            break
    for k in range(len(a)):
        if c == a[k][1]:
            d.append(a[k][0])
            d.sort()
    for l in d:
        print(l)



