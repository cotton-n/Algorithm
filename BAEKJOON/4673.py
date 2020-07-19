"""
셀프 넘버
"""

from sys import stdin

num_list = [True] * 10001
for i in range(1, 10001):
    if i < 10:
        num_list[i * 2] = False
    elif i < 100:
        string_num = str(i)
        total = i + int(string_num[0]) + int(string_num[1])
        num_list[total] = False
    elif i < 1000:
        string_num = str(i)
        total = i + int(string_num[0]) + int(string_num[1]) + int(string_num[2])
        num_list[total] = False
    else:
        string_num = str(i)
        total = i + int(string_num[0]) + int(string_num[1]) + int(string_num[2]) + int(string_num[3])
        if total <= 10000:
            num_list[total] = False

for i in range(1, 10001):
    if num_list[i]:
        print(i)