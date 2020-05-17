"""
후위 표기식 - 검색
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write

priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}


def solve(string):
    op = []
    for s in string:
        if 'A' <= s <= 'Z':
            sysOut(s)
        elif s == '(':
            op.append(s)
        elif s == ')':
            while op and op[-1] != '(':
                sysOut(op.pop())
            op.pop()
        else:
            while op and priority[s] <= priority[op[-1]]:
                sysOut(op.pop())
            op.append(s)
    while op:
        sysOut(op.pop())
    sysOut('\n')


if __name__ == '__main__':
    solve(sysIn.rstrip())
