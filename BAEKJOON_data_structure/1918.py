"""
후위 표기식
"""
import sys


def solution(st):
    answer = ''

    op = ''
    bop = ''  # 괄호 안 연산
    flag = 0
    bflag = 0  # 괄호안에있는것
    stack = []
    for s in st:
        if s == '(':
            bflag = 1
            print(s)
        elif s == ')':
            bflag = 0
            print(s)
        elif bflag == 1:
            # 괄호 안 일때
            print(s)
        elif s == '+' or s == '-' or s == '*' or s == '/':
            op = s
            flag = 1
        else:
            if flag == 1:
                stack.append(s)
                stack.append(op)
                flag = 0
            else:
                stack.append(s)
    answer = ''.join(stack)
    return answer


if __name__ == '__main__':
    string = sys.stdin.readline().rstrip()
    result = solution(string)
    print(result)
