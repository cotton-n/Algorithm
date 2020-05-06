import sys

n = int(sys.stdin.readline())

q = []
size = 0
for i in range(n):
    o = sys.stdin.readline().split()
    command = o[0]
    if command == "push":
        q.append(o[1])
        size += 1
    elif command == "pop":
        if size == 0:
            print(-1)
        else:
            print(q[0])
            del q[0]
            size -= 1
    elif command == "size":
        print(size)
    elif command == "empty":
        if size == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if size == 0:
            print(-1)
        else:
            print(q[0])
    else:
        if size == 0:
            print(-1)
        else:
            print(q[-1])
