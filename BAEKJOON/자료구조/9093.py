"""
단어 뒤집기
"""

import sys

n = int(sys.stdin.readline())

for i in range(n):
    words = sys.stdin.readline().split()
    wordsReverse = ''
    for word in words:
        sv = ''
        for char in word:
            sv = char + sv
        wordsReverse += sv + ' '
    print(wordsReverse)
