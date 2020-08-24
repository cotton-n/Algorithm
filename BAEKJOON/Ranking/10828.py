"""
스택
"""

from sys import stdin

n = int(stdin.readline().rstrip())

stack = list()
size = 0
for _ in range(n):
    cmd = stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])
        size += 1
    elif cmd[0] == 'pop':
        if size == 0:
            print('-1')
        else:
            print(stack.pop())
            size -= 1
    elif cmd[0] == 'size':
        print(size)
    elif cmd[0] == 'empty':
        if size == 0:
            print('1')
        else:
            print('0')
    else:
        if size == 0:
            print('-1')
        else:
            print(stack[-1])