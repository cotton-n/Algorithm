"""
조합 0의 개수 - 검색
0의 개수만 필요하다는 아이디어만 참고
시간 초과
"""
import sys
sysIn = sys.stdin.readline()


def solution(nums):
    a, b = map(int, nums.split())
    two1, five1 = 0, 0
    two2, five2 = 0, 0
    two3, five3 = 0, 0

    for i in range(2, a + 1):
        t, f = i // 2, i // 5
        two1 += t
        five1 += f
        if i <= b:
            two2 += t
            five2 += f
        if i <= a - b:
            two3 += t
            five3 += f

    return min(two1 - (two2 + two3), five1 - (five2 + five3))


if __name__ == '__main__':
    print(solution(sysIn.rstrip()))
