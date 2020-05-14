"""
후위 표기식
"""

# TODO: (a+b-c)*d*e 괄호 바로 오른쪽에 *이나 /가 있을 때 반례 생김
# TODO: 저 괄호 안에 있는 우선순위도 생각해줘야함
import sys


def cal(stack, o, f, n):
    flag = f
    op = o
    if n == '+' or n == '-' or n == '*' or n == '/':
        op.append(n)
        flag = 1
    else:
        if flag == 1:
            stack.append(n)
            if op:
                stack.append(op.pop())
            flag = 0
        else:
            stack.append(n)
    return [op, flag]


def solution(st):
    print(st)
    op = []
    b_op = []  # 괄호안 연산
    flag = 0
    b = 0  # 괄호안인지 아닌지
    p = 0  # 우선순위
    stack = []
    b_stack = []
    for s in st:
        if s == '(':
            b = 1
            p += 1
        elif s == ')':
            while b_op:
                b_stack.append(b_op.pop())
            p -= 1
            if p == 0:
                stack.append(''.join(b_stack))
                if op:
                    stack.append(op.pop())
                b_stack = []
                b = 0
        elif b == 1:
            # 괄호안 일때
            b_op, b_flag = cal(b_stack, b_op, 0, s)
        else:
            op, flag = cal(stack, op, flag, s)
    answer = ''.join(stack)
    return answer


if __name__ == '__main__':
    string = sys.stdin.readline().rstrip()
    size = len(string)
    string_stack = []
    i = 0
    while i < size:
        if (string[i] == '*' or string[i] == '/') and string[i+1] != '(':
            string_stack.append('('+string_stack.pop()+string[i]+string[i+1]+')')
            i += 2
        else:
            string_stack.append(string[i])
            i += 1
    result = solution(''.join(string_stack))
    print(result)
