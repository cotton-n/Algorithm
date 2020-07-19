"""
상수
"""
from sys import stdin

a, b = stdin.readline().rstrip().split()
if int(a[::-1]) < int(b[::-1]):
    print(b[::-1])
else:
    print(a[::-1])