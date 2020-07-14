"""
평균
"""

from sys import stdin

n = int(stdin.readline().rstrip())
score_list = list(map(int, stdin.readline().rstrip().split()))

max = 0
for score in score_list:
    if max < score:
        max = score

total = 0
for score in score_list:
    score = score / max * 100
    total += score
print(total / n)
        