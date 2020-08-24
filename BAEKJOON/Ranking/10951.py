"""
A + B - 4
"""

from sys import stdin

for line in stdin:
    a, b = map(int, line.split())
    print(a + b)
