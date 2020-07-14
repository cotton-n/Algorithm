"""
세 수
"""

from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())

if a >= b:
    if c >= a:
        print(a)
    elif b >= c:
        print(b)
    else:
        print(c)
else:
    if c > b:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)