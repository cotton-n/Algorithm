"""
단어 수학
"""

from sys import stdin

n = int(stdin.readline().rstrip())

words = list()
priority = dict() 
result = 0 
num = 9

for _ in range(n):
    word = stdin.readline().rstrip()
    i = 1
    length = len(word)
    for w in word:
        try:
            priority[w] += 10 ** (length - i)
        except KeyError:
            priority[w] = 10 ** (length - i)
        i += 1
    words.append(word)

priority = sorted(priority.items(), key=lambda x: -x[1])

for p in priority:
    result += num * p[1]
    num -= 1

print(result)

"""
11
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
BB

answer: 1889
"""
