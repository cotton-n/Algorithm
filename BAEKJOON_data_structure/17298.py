"""
오큰수
"""
import sys

n = int(sys.stdin.readline())
numList = map(int, sys.stdin.readline().rstrip().split())

maxNum = max(numList)
answer = []
flag = 0

for i, num in enumerate(numList):
    flag = 0
    if num == maxNum or (i+1) == n:
        answer.append(str(-1))
    else:
        for j in range(i+1, n):
            if num < numList[j]:
                answer.append(str(numList[j]))
                flag = 1
                break
        if flag == 0:
            answer.append(str(-1))

print(' '.join(answer))
