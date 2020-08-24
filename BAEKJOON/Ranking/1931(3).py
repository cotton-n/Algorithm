"""
회의실배정
"""

from sys import stdin

n = int(stdin.readline().rstrip())

time_list = list()

for _ in range(n):
    start, end = map(int, stdin.readline().rstrip().split())
    time_list.append([start, end, end-start])

time_list = sorted(time_list, key=lambda x: (x[1], x[0], x[2]))

count = 0
end_time = -1
for time in time_list:
    if end_time <= time[0]:
        end_time = time[1]
        count += 1

print(count)
