"""
오큰수(2) - 최종(소영 아이디어)
"""
import sys

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().rstrip().split()))
size = len(numList)

answer = []

for i in range(size):
    index = size - i - 1
    if index == size - 1:
        answer.append(str(-1))
    else:
        if numList[index + 1] > numList[index]:
            answer.append(str(numList[index + 1]))
        else:
            if answer[i - 1] == -1:
                answer.append(str(-1))
            elif answer[i - 1] == numList[index]:
                answer.append(str(answer[i - 2]))
            else:
                k = len(answer) - 1
                flag = 0
                while int(answer[k]) <= numList[index]:
                    if answer[k] == '-1':
                        answer.append(str(-1))
                        flag = 1
                        break
                    k -= 1
                if flag == 0:
                    answer.append(str(answer[k]))

answer.reverse()
print(' '.join(answer))
