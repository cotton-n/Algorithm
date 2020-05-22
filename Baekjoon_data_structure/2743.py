"""
단어 길이 재기
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write


def solve(string):
    c = len(string)
    sysOut(str(c))


if __name__ == '__main__':
    solve(sysIn.rstrip())
