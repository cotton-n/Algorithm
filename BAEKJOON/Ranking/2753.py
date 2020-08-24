"""
윤년
"""

from sys import stdin

year = int(stdin.readline().rstrip())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)