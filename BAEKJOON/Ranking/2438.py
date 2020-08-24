"""
별 찍기 - 1
"""

from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(1, n + 1):
    print('*' * i)