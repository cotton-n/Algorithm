"""
한수 
"""

from sys import stdin

n = int(stdin.readline().rstrip())

if n < 100:
    print(n)
else:
    def aber(n):
        string_num = str(n)
        if int(string_num[1]) - int(string_num[0]) == int(string_num[2]) - int(string_num[1]):
            return True
        else:
            return False
        

    result = 99
    for i in range(100, n + 1):
        # 한수인지 아닌지
        if aber(i):
            result += 1
    print(result)