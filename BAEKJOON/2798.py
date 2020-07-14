"""
블랙잭
"""

from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().rstrip().split())
card = list(map(int, stdin.readline().rstrip().split()))

com = combinations(card, 3)

answer = -1
for c in com:
    total = c[0] + c[1] + c[2]
    if total <= m and answer < total:
        answer = total

print(answer)