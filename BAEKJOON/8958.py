"""
OX퀴즈
"""

from sys import stdin

n = int(stdin.readline().rstrip())

for _ in range(n):
    result = stdin.readline().rstrip()
    total = 0
    before = 0 
    for r in result:
        if r == 'O':
            if before == 0:
                total += 1
                before += 1
            else:
                total += (before + 1)
                before += 1
        else:
            before = 0
    print(total)