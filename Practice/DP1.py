def solution(N, number):
    if N == number:
        return 1
    answer = 0
    # Memoization
    memo = [0 for i in range(number + 1)]
   
    memo[1] = 2 # 5/5, 2/2, ...
    memo[2] = 4 # 1+1, 5/5+5/5
    for i in range(N):
        pass

    # 최솟값이 8보다 크면 -1 반환
    if memo[number] >= 8:
        return -1

    return answer

if __name__ == "__main__":
    print(solution(5, 12)) # 4
    print(solution(2, 11)) # 3
