"""
구구단
"""

from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(1, 10):
    # (%s:문자열 %d:정수 %f:부동소수점)
    print('%d * %d = %d' %(n, i, n * i))