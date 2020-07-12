"""
접미사 배열
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write


def solve(string):
    answer = []
    i = 0
    for _ in string:
        answer.append(string[i:])
        i += 1

    answer.sort()
    for a in answer:
        sysOut(a + '\n')


if __name__ == '__main__':
    solve(sysIn.rstrip())
