"""
나이순 정렬
"""

from sys import stdin

n = int(stdin.readline().rstrip())

p_list = list()
for i in range(n):
    age, name = stdin.readline().rstrip().split()
    p_list.append([int(age), name, i])

p_list =  sorted(p_list, key=lambda x: (x[0], x[2]))

for p in p_list:
    print(p[0], p[1])