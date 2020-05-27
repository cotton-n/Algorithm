"""
ABCDE - 검색
"""
from sys import stdin


def dfs(cnt, nxt, graph, visited):
    global flag

    visited[nxt] = True
    if cnt == 4:
        flag = True
        return

    for i in graph[nxt]:
        if not visited[i]:
            dfs(cnt + 1, i, graph, visited)
            visited[i] = False


def solve(n):
    A, B = map(int, n.split())
    graph = [[] for _ in range(A)]
    visited = [False for _ in range(A)]

    for _ in range(B):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for r in range(A):
        dfs(0, r, graph, visited)
        visited[r] = False
        if flag:
            print(1)
            break

    else:
        print(0)


if __name__ == '__main__':
    flag = False
    solve(stdin.readline().rstrip())
