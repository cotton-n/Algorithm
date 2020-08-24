"""
평균 점수
"""

from sys import stdin

total_score = 0
for _ in range(5):
    score = int(stdin.readline().rstrip())
    if score < 40:
        score = 40
    total_score += score

print(int(total_score / 5))