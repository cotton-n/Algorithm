"""
팩토리얼
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


def solve(n):
    answer = factorial(int(n))
    sysOut(str(answer))


if __name__ == '__main__':
    solve(sysIn.rstrip())
