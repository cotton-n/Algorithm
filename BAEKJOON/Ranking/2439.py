"""
별 찍기 - 2
"""

from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(1, n + 1):
    print(' ' * (n - i), end = '')
    print('*' * i)