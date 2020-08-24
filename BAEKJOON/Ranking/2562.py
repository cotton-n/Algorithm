"""
최댓값
"""

from sys import stdin

max = -1
index = -1
for i in range(1, 10):
    n = int(stdin.readline().rstrip())
    if max < n:
        index = i
        max = n
print(max)
print(index)