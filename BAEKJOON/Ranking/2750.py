"""
수 정렬하기
"""

from sys import stdin

n = int(stdin.readline().rstrip())
num_list = list()
for _ in range(n):
    num_list.append(int(stdin.readline().rstrip()))
num_list.sort()
for num in num_list:
    print(num)