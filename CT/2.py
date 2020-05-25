from itertools import permutations


def solution(n):
    answer = []
    ans = []
    size = 0
    for i in range(n // 2 + 1):
        answer.append(3 ** i)
        size += 1
        for j in range(2, size + 1):
            ans.extend(list(permutations(answer, j)))
    ans = set(ans)
    for a in ans:
        total = 0
        for i in a:
            total += i
        answer.append(total)
    answer = sorted(set(answer))
    return answer[n-1]


if __name__ == '__main__':
    print(solution(4))
    print(solution(11))
