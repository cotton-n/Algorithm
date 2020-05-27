"""
ABCDE - 스스로
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
    N, M = map(int, n.split())
    graph = [[] for _ in range(N)]
    visited = [False for _ in range(N)]

    for _ in range(M):
        a, b = map(int, stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        if flag:
            print(1)
            return
        else:
            dfs(0, i, graph, visited)
            visited[i] = False

    print(0)


if __name__ == '__main__':
    flag = False
    solve(stdin.readline().rstrip())
