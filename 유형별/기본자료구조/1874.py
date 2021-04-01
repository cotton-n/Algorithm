'''
스택 수열
'''

import sys

n = int(sys.stdin.readline())
listA = list()
stack = list()
answer = list()

for _ in range(n):
  listA.append(int(sys.stdin.readline()))

startIndex = 0
size = 0
index = 0
i = 1
while startIndex < n and i <= n + 1:
  if size != 0 and stack[-1] == listA[startIndex]:
    stack.pop()
    startIndex += 1
    size -= 1
    answer.append('-');
    index += 1
  else: 
    stack.append(i)
    size += 1
    answer.append('+');
    i += 1

if startIndex != n: print('NO')
else: print('\n'.join(answer))