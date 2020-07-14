"""
숫자의 개수
"""

from sys import stdin

multi = 1

for _ in range(3):
    multi *= int(stdin.readline().rstrip())

str_num = str(multi)
exist_list = [0 for _ in range(10)]

for s in str_num:
    exist_list[int(s)] += 1

for exist in exist_list:
    print(exist)
