"""
조합 0의 개수
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write

#  TODO: nCm 계산하는 함수 만들기


def solve(n):
    a, b = map(int, n.split())
    print(a, b)


if __name__ == '__main__':
    solve(sysIn.rstrip())
