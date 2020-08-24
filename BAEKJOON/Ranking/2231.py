"""
분해합
"""
from sys import stdin

n = int(stdin.readline().rstrip())

answer = [0] * 1000001

for i in range(1, n + 1):
    if i < 10:
        answer[i * 2] = i
    else:
        str_num = str(i)
        total = i
        for num in str_num:
            total += int(num)
        if total < 1000001 and answer[total] == 0:
            answer[total] = i
print(answer[n])