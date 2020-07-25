"""
팩토리얼 0의 개수
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
    f = factorial(int(n))
    sList = list(str(f))
    sList.reverse()
    for i, s in enumerate(sList):
        if s != '0':
            sysOut(str(i))
            break


if __name__ == '__main__':
    solve(sysIn.rstrip())
