"""
상하좌우
"""

n = int(input())
move_list = list(input().split())
move = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}

current = [1, 1]
for m in move_list:
    if 0 < current[0] + move[m][0] <= n and 0 < current[1] + move[m][1] <= n:
        current = [current[0] + move[m][0], current[1] + move[m][1]]

for position in current:
    print(position, end=' ')
