"""
오등큰수
"""
import sys

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().rstrip().split()))
size = len(numList)

answer = []

numDic = {}
for num in numList:
    try:
        numDic[num] += 1
    except KeyError:
        numDic[num] = 1

for i in range(size):
    index = size - i - 1
    if index == size - 1:
        answer.append(str(-1))
    else:
        if numDic[numList[index + 1]] > numDic[numList[index]]:
            answer.append(str(numList[index + 1]))
        else:
            if answer[i - 1] == '-1':
                answer.append(str(-1))
            else:
                k = len(answer) - 1
                while answer[k] != '-1' and numDic[int(answer[k])] <= numDic[numList[index]]:
                    k -= 1
                answer.append(str(answer[k]))

answer.reverse()
print(' '.join(answer))
