"""
거스름돈
"""

money = int(input())
coins = [500, 100, 50, 10, 5, 1]

change = 1000 - money

result = 0
for coin in coins:
    result += change // coin
    change %= coin

print(result)
    