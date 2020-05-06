import sys

n = int(sys.stdin.readline())

a = []
length = 0

for i in range(n):
    op = sys.stdin.readline().split()
    s = ''
    if len(op) == 2:
        #  push
        a.append(op[1])
        length += 1
        continue
    else:
        s = op[0]
    #  pop
    if s == 'pop':
        if length == 0:
            print('-1')
            continue
        else:
            print(a.pop())
            length -= 1
            continue
    #  size
    if s == 'size':
        print(length)
        continue
    #  empty
    if s == 'empty':
        if length == 0:
            print('1')
            continue
        else:
            print('0')
            continue
    #  top
    if s == 'top':
        if length == 0:
            print('-1')
            continue
        else:
            print(a[-1])
            continue
