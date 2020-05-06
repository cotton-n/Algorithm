def solution(n):
    answer = [0]

    for i in range(n - 1):
        answer = [j for sub in ([0] + [answer[i]] + [1] if i % 2 == 0 else [answer[i]] for i in range(len(answer)))
                  for j in sub]

    return answer


if __name__ == "__main__":
    print(solution(3))
