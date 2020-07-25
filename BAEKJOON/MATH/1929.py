"""
소수 구하기 (에라토스테네스의 체)
"""
import math
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write


def prime(numList, num):
    length = math.ceil(math.sqrt(num))
    for n in range(2, length):
        if numList[n]:
            for k in range(n + n, num + 1, n):
                numList[k] = False


def solve(s):
    a, b = map(int, s.split())
    ans = [True] * (b + 1)
    prime(ans, b)
    ans[0] = False
    ans[1] = False
    for i in range(a, b+1):
        if ans[i]:
            sysOut(str(i) + '\n')


if __name__ == '__main__':
    solve(sysIn.rstrip())
