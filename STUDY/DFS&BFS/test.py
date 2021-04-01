# BFS
from collections import deque

def canDownLotate(graph, current):
    if graph[current]

def bfs(a1, b1, a2, b2, graph, n):    
    queue = deque()
    queue.append((a1, b1, a2, b2))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [(0, 0, 0, 1), (0, 1, 0, 0)]
    
    while queue:
        x1, y1, x2, y2 = queue.popleft()
        
        for i in range(8):
            if i < 4:
                nx1 = x1 + dx[i]
                ny1 = y1 + dy[i]
                nx2 = x2 + dx[i]
                ny2 = y2 + dy[i]
            elif i == 4:
                nx1 = x1
                ny1 = y1
                nx2 = x1 + 1
                ny2 = y1
            elif i == 5:
                nx1 = x2 + 1
                ny1 = y2
                nx2 = x2
                ny2 = y2
            elif i == 6:
                nx1 = x1
                ny1 = y1
                nx2 = x1 - 1
                ny2 = y1
            elif i == 7:
                nx1 = x2 - 1
                ny1 = y2
                nx2 = x2
                ny2 = y2

            if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= n:
                continue
            
            if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= n:
                continue

            if (nx1, ny1, nx2, ny2) in visited:
                continue

            if graph[nx1][ny1] == 1 or graph[nx2][ny2] == 1:
                a = min(graph[x1][y1] + 1, graph[x2][y2] + 1)
                graph[nx1][ny1] = a
                graph[nx2][ny2] = a
                queue.append((nx1, ny1, nx2, ny2))
                visited.append((nx1, ny1, nx2, ny2))
                visited.append((nx2, ny2, nx1, ny1))
                print(nx1, ny1, nx2, ny2)
                print(graph[nx1][ny1], graph[nx2][ny2])

    return graph[n - 1][n - 1]

def solution(board):
    n = len(board)
    new_board = []
    for b in board:
        temp = []
        for a in b:
            if a == 0:
                temp.append(1)
            else:
                temp.append(0)
        new_board.append(temp)
    
    answer = bfs(0, 0, 0, 1, new_board, n)
    return answer - 1

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])