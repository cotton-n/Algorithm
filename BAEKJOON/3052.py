"""
나머지
"""

from sys import stdin

remain = dict()

for _ in range(10):
    num = int(stdin.readline().rstrip())
    try:
        remain[num % 42] += 1
    except KeyError:
        remain[num % 42] = 1

print(len(remain))