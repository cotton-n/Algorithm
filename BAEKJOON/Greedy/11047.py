"""
동전 0
"""

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

result = 0
for i in range(len(coins) - 1, -1, -1):
    result += k // coins[i]
    k = k % coins[i]

print(result)
