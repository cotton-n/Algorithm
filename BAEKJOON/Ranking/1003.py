"""
피보나치 함수
"""

from sys import stdin

t = int(stdin.readline().rstrip())

fibo_list = [(1, 0)] * 41
fibo_list[1] = (0, 1)

for i in range(2, 41):
    fibo_list[i] = (fibo_list[i-2][0] + fibo_list[i-1][0], fibo_list[i-2][1] + fibo_list[i-1][1])

for _ in range(t):
    n = int(stdin.readline().rstrip())
    print(fibo_list[n][0], fibo_list[n][1])
