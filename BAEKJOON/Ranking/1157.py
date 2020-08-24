"""
단어 공부
"""

from sys import stdin

string = stdin.readline().rstrip().upper()

if len(string) == 1:
    print(string)
else:
    alpha = dict()

    for s in string:
        try:
            alpha[s] += 1
        except KeyError:
            alpha[s] = 1

    alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True)

    if alpha[0][1] == alpha[1][1]:
        print('?')
    else:
        print(alpha[0][0])
