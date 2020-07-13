"""
별 찍기 - 9
"""

from sys import stdin

n = int(stdin.readline().rstrip())
a = 0
b = 0 
for i in range(2 * n - 1):
    print(' ' * b, end='')
    print('*' * ((2 * n - 1) - a))
    if i < n - 1:
        a += 2
        b += 1
    else:
        a -= 2
        b -= 1