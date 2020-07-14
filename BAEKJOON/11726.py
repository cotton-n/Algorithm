"""
2 × n 타일링
"""

from sys import stdin

n = int(stdin.readline().rstrip())

def num_way(n):
    result = list()
    for i in range(n + 1):
        if i < 3:
            result.append(i)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result[n]
    
print(num_way(n) % 10007)