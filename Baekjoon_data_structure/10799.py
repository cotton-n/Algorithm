"""
쇠막대기
"""

import sys

iron = sys.stdin.readline().rstrip()

flag = 0
answer = 0
# 얼마를 더해야 하는지 
c = 0

for i in iron:
    if i == '(':
        c += 1
        flag = 1
    else:
        c -= 1
        if flag == 1:
            answer += c
            flag = 0
        else:
            answer += 1
            
print(answer)