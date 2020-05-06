"""
괄호
"""

import sys

n = int(sys.stdin.readline())

for i in range(n):
    bracket = sys.stdin.readline()
    a = []
    length = 0
    flag = 0
    for b in bracket:
        if b == '\n':
            break
        if b == ')' and length == 0:
            print('NO')
            flag = 1
            break
        elif b == ')':
            a.pop()
            length -= 1
        else:
            a.append(b)
            length += 1
    if length != 0:
        print('NO')
    elif flag == 1:
        continue
    else:
        print('YES')
