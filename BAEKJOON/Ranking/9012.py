"""
괄호
"""

from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
    bracket = stdin.readline().rstrip()
    stack = list()
    size = 0
    flag = True
    for b in bracket:
        if b == '(':
            stack.append(b)
            size += 1
        else:
            if size == 0:
                flag = False
                break
            stack.pop()
            size -= 1
    if not flag or size > 0:
        print('NO')
    else:
        print('YES')