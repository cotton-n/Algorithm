"""
1로 만들기
"""
from sys import stdin

n = int(stdin.readline().rstrip())

sum_list = [1000001]

def make_one(num, result):
    if num == 1:
        if sum_list[0] > result:
            sum_list[0] = result
        return 1
    if num < 1:
        return 0
    if sum_list[0] > result:
        if num % 3 == 0 and num % 2 == 0:
            make_one(num // 3, result + 1)
            make_one(num // 2, result + 1) 
            make_one(num - 1, result + 1)
        elif num % 3 == 0:
            make_one(num // 3, result + 1) 
            make_one(num - 1, result + 1)
        elif num % 2 == 0:
            make_one(num // 2, result + 1) 
            make_one(num - 1, result + 1)
        else:
            make_one(num - 1, result + 1)

make_one(n, 0)
print(sum_list[0])