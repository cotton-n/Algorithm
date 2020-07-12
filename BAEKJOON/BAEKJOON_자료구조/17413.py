"""
단어 뒤집기2
"""

import sys

string = sys.stdin.readline().rstrip()
string += ' '
answer = []
word = []  # stack

# 태그인지 아닌지를 판별할 수 있는 변수 
flag = 0
for s in string:
    if s == ' ' or s == '<':
        if s == '<':
            flag = 1
        while word:
            # print(word)
            answer.append(word.pop())
        answer.append(s)
    elif flag == 0:
        word.append(s)
    elif flag == 1:
        if s == '>':
            flag = 0
        answer.append(s)
    # print(list(answer.queue))
    
answerString = ''
for a in answer:
    answerString += a

print(answerString)
