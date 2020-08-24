"""
소수 구하기
"""
from sys import stdin

m, n = map(int, stdin.readline().rstrip().split())

prime = [True] * (n + 1)
prime[0] = False
prime[1] = False
prime[2] = True

for i in range(2, n + 1):
    if prime[i]: # True일 때 
        for j in range(i + i, n + 1, i):
            prime[j] = False 

for i in range(m, n + 1):
    if prime[i]:
        print(i)