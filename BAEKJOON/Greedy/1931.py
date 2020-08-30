"""
회의실 배정 - 보류
"""

n = int(input())
time_table = list()
for _ in range(n):
    start, end = map(int, input().split())
    time_table.append([start, end])

time_table = sorted(time_table, key=lambda x: (x[0], x[1]))

result = [time_table[0]]
size = len(time_table)
for i in range(1, size):
    if result[-1][1] > time_table[i][0] and result[-1][1] > time_table[i][1]:
        result.pop()
        result.append(time_table[i])
    elif time_table[i][0] >= result[-1][1]:
        result.append(time_table[i])

print(len(result))

"""
반례

5
4 4
4 4
3 4
2 4
1 4

answer : 3

3
7 7
7 8
8 8

answer : 3
"""