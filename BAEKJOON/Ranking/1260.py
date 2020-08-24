"""
DFS와 BFS
"""

from sys import stdin

n, m, v = map(int, stdin.readline().rstrip().split())

graph = dict()

for i in range(1, n + 1):
    graph[i] = list()

for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(graph, start_node):
    visited = list()
    stack = list()
    stack.append(start_node)
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            stack.extend(list(reversed(graph[current_node])))
    return visited

def bfs(graph, start_node):
    visited = list()
    queue = list()
    queue.append(start_node)
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
            queue.extend(graph[current_node])
    return visited

dfs_list = dfs(graph, v)
bfs_list = bfs(graph, v)

for i in dfs_list:
    print(i, end = ' ')
print()
for i in bfs_list:
    print(i, end = ' ')
