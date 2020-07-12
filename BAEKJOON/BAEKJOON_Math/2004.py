"""
조합 0의 개수(X)
런타임 에러 - 재귀호출때문
n, m(0≤m≤n≤2,000,000,000, n!=0)
n = 2000000000 이거 대입해보면 됨
"""
import sys
sysIn = sys.stdin.readline()


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


def permutation(n, r):
    return factorial(n)/factorial(n-r)


def combination(n, r):
    return permutation(n, r)/factorial(r)


def solution(nums):
    a, b = map(int, nums.split())
    comb = str(int(combination(a, b)))

    answer = 0

    for c in comb:
        if c == '0':
            answer += 1
        else:
            answer = 0

    return answer


if __name__ == '__main__':
    print(solution(sysIn.rstrip()))
