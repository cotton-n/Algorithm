"""
A + B - 8
"""

from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    print("Case #%d: %d + %d = %d" %(i+1, a, b, a + b))