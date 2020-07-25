"""
문자열 분석 - 소영 도움
"""
from sys import stdin, stdout


def solve(string):
    answer = [0, 0, 0, 0]  # [소문자, 대문자, 숫자, 공백]
    for s in string:
        if 'a' <= s <= 'z':
            answer[0] += 1
        elif 'A' <= s <= 'Z':
            answer[1] += 1
        elif '0' <= s <= '9':
            answer[2] += 1
        else:
            answer[3] += 1

    stdout.write(' '.join([str(n) for n in answer]) + '\n')


if __name__ == '__main__':
    #  반복 입력
    for st in stdin:
        solve(st.rstrip('\n'))
