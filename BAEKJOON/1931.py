"""
회의실배정
"""

# ! 시간초과
from sys import stdin

n = int(stdin.readline().rstrip())
time_list = list()
time_list_length = 0
for _ in range(n):
    start, end = map(int, stdin.readline().rstrip().split())
    time_list.append([start, end])
    time_list_length += 1

time_list.sort()

meeting_room = []
def room_assignment(time, index, time_size):
    print(time)
    if time[-1][1] > time_list[-1][0]:
        if meeting_room == []:
            meeting_room.append(time_size)
            return
        if meeting_room[-1] < time_size:
            meeting_room.append(time_size)
            return
    for i in range(index, time_list_length):
        if time[-1][1] <= time_list[i][0]:
            time.append(time_list[i])
            time_size += 1
            room_assignment(time, index + 1, time_size)
            time.pop()
            time_size -= 1

for i in range(time_list_length):
    room_assignment([time_list[i]], i, 1)
    if time_list_length - meeting_room[-1] == i:
        break
print(meeting_room[-1])

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