"""
숫자의 합
"""

from sys import stdin

n = int(stdin.readline().rstrip())
string = stdin.readline().rstrip()
total = 0
for s in string:
    total += int(s)

print(total)