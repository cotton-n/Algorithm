"""
사분면 고르기
"""

from sys import stdin

x = int(stdin.readline().rstrip())
y = int(stdin.readline().rstrip())

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else:
    print(3)