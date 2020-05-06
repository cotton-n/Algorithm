"""
에디터(2) - 최종
"""

import sys

string = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

left = list(string)
right = []

print(left, right)

for i in range(n):
    o = sys.stdin.readline().rstrip()
    com = o[0]
    if com == "L" and left:
        right.append(left.pop())
    elif com == "D" and right:
        left.append(right.pop())
    elif com == "B" and left:
        left.pop()
    else:
        if com == "P":
            left.append(o[2])

total = left + right[::-1]
print(''.join(total))
