"""
별 찍기 - 13
"""

from sys import stdin

n = int(stdin.readline().rstrip())
a = 1
for i in range(2 * n - 1):
    print('*' * a)
    if i < n - 1:
        a += 1
    else:
        a -= 1