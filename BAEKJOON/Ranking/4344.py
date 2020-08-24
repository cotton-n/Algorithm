"""
평균은 넘겠지
"""

from sys import stdin

c = int(stdin.readline().rstrip())

for _ in range(c):
    case = list(map(int, stdin.readline().rstrip().split()))
    total = 0
    for score in case[1:]:
        total += score
    avg = total / case[0]
    person = 0
    for score in case[1:]:
        if score > avg:
            person += 1
    print(format(round(person / case[0] * 100, 3), ".3f")+'%')
