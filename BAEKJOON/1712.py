"""
손익분기점
"""

from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())
if b >= c:
    print(-1)
else:
    print(int(a / (c - b)) + 1)
