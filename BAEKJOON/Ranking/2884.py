"""
알람 시계
"""

import sys

h, m = map(int, sys.stdin.readline().rstrip().split())

m = m - 45

if m < 0:
    m = 60 + m
    h = h - 1
    if h < 0:
        h = 24 + h 
print(h, m)
