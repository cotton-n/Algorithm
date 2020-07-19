"""
회의실배정
"""

from sys import stdin

n = int(stdin.readline().rstrip())
time_list = list()
for _ in range(n):
    start, end = map(int, stdin.readline().rstrip().split())
    time = end - start
    time_list.append((start, end, time))

time_list = sorted(time_list, key=lambda x: (x[0],x[1]))

print(time_list)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
(1,4), (5,7), (8,11), (12,14)
"""