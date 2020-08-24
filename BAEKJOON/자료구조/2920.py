"""
음계
"""

from sys import stdin

num_list = list(map(int, stdin.readline().rstrip().split()))

flag = True
for i in range(7):
    if abs(num_list[i + 1] - num_list[i]) != 1:
        flag = False
        break

if flag:
    if num_list[0] == 1:
        print("ascending")
    else:
        print("descending")
else:
    print("mixed")
    