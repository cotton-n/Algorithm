"""
조합 0의 개수 - 검색
0의 개수만 필요하다는 아이디어만 참고
메모리초과
"""
import sys
sysIn = sys.stdin.readline()


# 2와 5의 개수를 얻는 함수
def count_twoFive(n):
    two = 0
    five = 0
    while n % 2 == 0 or n % 5 == 0:
        if n % 2 == 0:
            n = n / 2
            two += 1
        if n % 5 == 0:
            n = n / 5
            five += 1
    return [two, five]


def factorial_twoFive(n):
    two = 0
    five = 0
    for i in range(2, n+1):
        t, f = count_twoFive(i)
        two += t
        five += f
        d[i] = [two, five]
    return [two, five]


def solution(nums):
    answer = 0
    a, b = map(int, nums.split())
    global d
    d = [[-1, -1] for _ in range(a + 1)]

    two1, five1 = factorial_twoFive(a)
    two2, five2 = d[a-b]
    two3, five3 = d[b]
    two = two1 - (two2 + two3)
    five = five1 - (five2 + five3)
    if two == 0 or five == 0:
        return 0
    else:
        while two != 0 and five != 0:
            two -= 1
            five -= 1
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(sysIn.rstrip()))
