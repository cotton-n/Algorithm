"""
빠른 A + B
"""

from sys import stdin

n = int(stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    print(a + b)