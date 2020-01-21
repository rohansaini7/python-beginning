"""
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values. The user enters some integer  followed by the names
and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name.
 Output the average percentage marks obtained by that student, correct to two decimal places.
"""

if __name__ == '__main__':
    total=0

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #
        scores = list(map(float, line))
        student_marks[name] = scores # key->name , ki value h score?
    query_name = input()
    if student_marks[query_name] != None:
        a=len(scores)
        print(a)
        for i in student_marks[query_name]:
            total=total+i
        b=float(total/a)
        print('{:.2f}'.format(b))

    else:
        print("it is not in dic")
