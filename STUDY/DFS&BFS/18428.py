"""
감시 피하기
"""

n = int(input())
graph = []
o_count = 3

for _ in range(n):
    graph.append(list(input().split()))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n or graph[x][y] == 'O':
        return 
    if graph[x + 1][y] == 'S':
        graph[x][y] = 'O'
        o_count -= 1
    return

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            print(dfs(i, j))
