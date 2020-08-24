"""
A + B - 3
"""

from sys import stdin

n = int(stdin.readline().rstrip())
num_list = list()

for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    num_list.append(a + b)

for i in range(n):
    print(num_list[i])
