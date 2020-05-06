import sys
from collections import deque

n = int(sys.stdin.readline())

li = []
li = deque(li)
size = 0

for i in range(n):
    s = sys.stdin.readline().rstrip().split()
    command = s[0]
    if command == 'push_front':
        li.appendleft(s[1])
        size += 1
    elif command == 'push_back':
        li.append(s[1])
        size += 1
    elif command == 'pop_front':
        if size == 0:
            print(-1)
        else:
            print(li.popleft())
            size -= 1
    elif command == 'pop_back':
        if size == 0:
            print(-1)
        else:
            print(li.pop())
            size -= 1
    elif command == 'size':
        print(size)
    elif command == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if size == 0:
            print(-1)
        else:
            print(li[0])
    elif command == 'back':
        if size == 0:
            print(-1)
        else:
            print(li[-1])