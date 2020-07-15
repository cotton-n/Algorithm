"""
문자열 반복
"""

from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
    r, s = stdin.readline().rstrip().split()
    r = int(r)

    result = ''
    for char in s:
        result += char * r
    print(result)