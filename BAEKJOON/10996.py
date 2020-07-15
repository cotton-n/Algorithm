"""
별 찍기 - 21
"""

from sys import stdin

n = int(stdin.readline().rstrip())

if n == 1:
    print('*')

else:
    star_shape = ''
    star = (n - 1) // 2 + 1
    for i in range(star * 2):
        if i % 2 == 0:
            star_shape += '*'
        else:
            star_shape += ' '
    # 줄바꿈 추가
    star_shape += '\n'
    if n % 2 != 0:
        star -= 1
    for i in range(star * 2):
        if i % 2 == 0:
            star_shape += ' '
        else:
            star_shape += '*'
    for _ in range(n):
        print(star_shape)
