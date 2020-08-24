"""
수 정렬하기 3
"""

from sys import stdin

# counting sort 방법
n = int(stdin.readline().rstrip())
count = [0] * 10001

for _ in range(n):
    count[int(stdin.readline().rstrip())] += 1

for i in range(10001):
    if count[i] != 0:
        print(('%d\n' % (i)) * count[i], end="")
