"""
회의실배정
"""

# ! 시간초과
from sys import stdin

n = int(stdin.readline().rstrip())

time_list = list()

for _ in range(n):
    start, end = map(int, stdin.readline().rstrip().split())
    time_list.append([start, end])

time_list.sort()

time_list2 = []
time_list2_length = 0
i = 0
while i < n:
    time_list2.append(time_list[i])
    time_list2_length += 1
    if i != n - 1 and time_list[i][0] == time_list[i + 1][0]:
        i += 2
    else:
        i += 1

i = 0
time_list.clear()
time_list_length = 0
while i < time_list2_length:
    if i != time_list2_length - 1 and time_list2[i][1] >= time_list2[i + 1][1]:
        time_list.append(time_list2[i + 1])
        i += 2
    else:
        time_list.append(time_list2[i])
        i += 1
    time_list_length += 1

i = time_list_length - 1
meeting_room_dic = {}
meeting_room_dic[time_list[i][0]] = 1
answer = 0
while i >= 0:
    for j in range(i, time_list_length):
        if time_list[i][1] <= time_list[j][0]:
            meeting_room_dic[time_list[i][0]] = 1 + meeting_room_dic[time_list[j][0]]
            if answer < meeting_room_dic[time_list[i][0]]:
                answer = meeting_room_dic[time_list[i][0]]
            break
    i -= 1

print(answer)
