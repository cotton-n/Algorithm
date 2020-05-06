"""
스택 수열(2) - 최종
"""

import sys

n = int(sys.stdin.readline())
stack = []
answer = []
d = 1
nextNum = 1
length = 0
for j in range(n):
    num = int(sys.stdin.readline())
    try:
        if length != 0 and nextNum != 1 and stack[-1] == num:
            stack.pop()
            length -= 1
            answer.append('-')
            continue

        k = nextNum
        if num >= nextNum:
            for i in range(k, num + 1):
                stack.append(i)
                length += 1
                answer.append('+')
                nextNum += 1
            stack.pop()
            length -= 1
            answer.append('-')
        else:
            print('NO')
            sys.exit(0)
    except IndexError:
        print('NO')
        sys.exit(0)
    # print(k, nextNum)
    # print(answer)
    # print(stack)

for a in answer:
    print(a)
