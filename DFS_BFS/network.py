def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(index):
        visited[index] = 1
        for nxt in range(n):
            if visited[nxt] == 0 and computers[index][nxt] == 1:
                dfs(nxt)

    for i, v in enumerate(visited):
        if v == 1:
            continue
        dfs(i)
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
