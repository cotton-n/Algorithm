"""
상근날드
"""

from sys import stdin

min_ham = 2001
min_drink = 2001
for i in range(5):
    price = int(stdin.readline().rstrip())
    if i <= 2:
        if min_ham > price:
            min_ham = price
    else:
        if min_drink > price:
            min_drink = price
print(min_drink + min_ham - 50)