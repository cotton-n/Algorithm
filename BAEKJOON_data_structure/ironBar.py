import sys

iron = sys.stdin.readline().rstrip()

answer = 0
# 얼마를 더해야 하는지 
c = 0

for i in iron:
    print(i)
    if i == '(':
        c += 1
    else:
        c -= 1
        answer += c