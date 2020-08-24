"""
사칙연산
"""

from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())

print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)