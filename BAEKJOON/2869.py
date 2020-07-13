"""
달팽이는 올라가고 싶다
"""

from sys import stdin
import math

a, b, v = map(int, stdin.readline().rstrip().split())
print(int(math.ceil((v - a) / (a - b))) + 1) 