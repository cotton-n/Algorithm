"""
곱셈
"""

from sys import stdin

x = int(stdin.readline().rstrip())
y = stdin.readline().rstrip()

print(x * int(y[2]))
print(x * int(y[1]))
print(x * int(y[0]))
print(x * int(y))