"""
네 수
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write


def solve(string):
    A, B, C, D = string.split()
    a = A + B
    b = C + D
    answer = int(a) + int(b)
    sysOut(str(answer))


if __name__ == '__main__':
    solve(sysIn.rstrip())
