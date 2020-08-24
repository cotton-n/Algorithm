"""
설탕 배달
"""

from sys import stdin

n = int(stdin.readline().rstrip())
count = 0
while True:
    if n % 5 == 0:
        break
    if n < 0:
        count = -1
    n -= 3
    count += 1

if n != 0:
    count += (n // 5)
print(count)
