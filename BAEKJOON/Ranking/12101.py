"""
1, 2, 3 더하기 2
"""

from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
answer = []
def recursive(goal, num_list, answer):
    if sum(num_list) == goal:
        answer.append(num_list[:])
        return 
    if sum(num_list) >= goal:
        return 
    for i in range(1, 4):
        num_list.append(i)
        recursive(goal, num_list, answer)
        num_list.pop()

recursive(n, [], answer)
try:
    print("+".join(map(str, answer[k-1])))
except IndexError:
    print(-1)