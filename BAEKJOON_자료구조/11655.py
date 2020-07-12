"""
ROT13
"""
from sys import stdin, stdout
sysIn = stdin.readline()
sysOut = stdout.write


def solve(string):
    answer = ''
    alpha = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
        'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
    }
    r_alpha = {}
    for key, value in alpha.items():
        r_alpha[value] = key

    for s in string:
        if 'a' <= s <= 'z':
            answer += r_alpha[(alpha[s] + 13) % 26]
        elif 'A' <= s <= 'Z':
            s = s.lower()
            answer += r_alpha[(alpha[s] + 13) % 26].upper()
        else:
            answer += s
    sysOut(answer)


if __name__ == '__main__':
    solve(sysIn.rstrip())
