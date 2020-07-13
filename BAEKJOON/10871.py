"""
X보다 작은 수
"""

from sys import stdin

n, x = map(int, stdin.readline().rstrip().split())
num_list = list(map(int, stdin.readline().rstrip().split()))

for num in num_list:
    if num < x:
        print(num, end=' ')