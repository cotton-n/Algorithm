"""
최소, 최대
"""

from sys import stdin

n = int(stdin.readline().rstrip())
num_list = list(map(int, stdin.readline().rstrip().split()))

max = -1000001
min = 1000001

for num in num_list:
    if min > num:
        min = num
    if max < num:
        max = num
print(min, max)