# 시간초과
import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

stack = []
index = 0
i = 1
flag = 0
answer = []
while True:
    if index == n and i-index == 1:
        flag = 1
        break
    if i == n+1 and stack[-1] != num[index]:
        break
    if i <= num[index]:
        stack.append(i)
        i += 1
        answer.append('+')
        continue
    if stack[-1] == num[index]:
        stack.pop()
        index += 1
        answer.append('-')

if flag == 0:
    print('NO')
else:
    for a in answer:
        print(a)
