"""
후위 표기식2
"""
import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

num = []
dic = {}
for i in range(n):
    num.append(int(sys.stdin.readline()))

i = 0
for s in string:
    if s != '+' and s != '-' and s != '*' and s != '/':
        try:
            if dic[s]:
                continue
        except KeyError:
            dic[s] = num[i]
            i += 1
stack = []
for s in string:
    if s == '+' or s == '-' or s == '*' or s == '/':
        x = stack.pop()
        y = stack.pop()
        if s == '+':
            stack.append(y + x)
        elif s == '-':
            stack.append(y - x)
        elif s == '*':
            stack.append(y * x)
        else:
            stack.append(y / x)
    else:
        stack.append(dic[s])

print(format(stack[0], ".2f"))
