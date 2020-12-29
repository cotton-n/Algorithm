"""
게임 개발
"""

n, m = map(int, input().split())
a, b, d = map(int, input().split())

full_map = list()
visited = [[0] * m for _ in range(n)]
visited[a][b] = 1

for _ in range(n):
    temp = list(map(int, input().split()))
    full_map.append(temp)

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

count = 1
turn = 0
while True:
    d -= 1
    if d == -1:
        d = 3
    turn += 1
    na = a + da[d]
    nb = b + db[d]
    if visited[na][nb] == 0 and full_map[na][nb] == 0:
        a = na
        b = nb
        visited[a][b] = 1
        turn = 0
        count += 1
        continue
    else:
        turn += 1
    if turn == 4:
        na = a - da[d]
        nb = b - db[d]
        if full_map[na][nb] == 0:
            a = na
            b = nb
            turn = 0
        else:
            break

print(count)
