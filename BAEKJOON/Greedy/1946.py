"""
신입 사원
"""

from sys import stdin

t = int(stdin.readline().rstrip())

grades = list()

for _ in range(t):
    n = int(stdin.readline().rstrip())
    grade = list()
    temp = list()
    for _ in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        temp.append([a, b])
    temp = sorted(temp, key=lambda x: x[0])
    grade.append(temp[0])
    for t in temp:
        if grade[-1][0] > t[0] or grade[-1][1] > t[1]:
            grade.append(t)
    grades.append(len(grade))

for grade in grades:
    print(grade)

"""
1
6
6 4
4 1
5 2
1 6
2 3
3 5

answer: 3
"""
