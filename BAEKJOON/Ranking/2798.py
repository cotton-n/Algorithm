"""
블랙잭
"""

# from sys import stdin
# from itertools import combinations

# n, m = map(int, stdin.readline().rstrip().split())
# card = list(map(int, stdin.readline().rstrip().split()))

# com = combinations(card, 3)

# answer = -1
# for c in com:
#     total = c[0] + c[1] + c[2]
#     if total <= m and answer < total:
#         answer = total

# print(answer)

n, m = map(int, input().split())
card = list(map(int, input().split()))

result = 0
length = len(card)

count = 0
for i in range(0, length - 2):
    for j in range(i + 1, length - 1):
        for k in range(j + 1, length):
            sum_value = card[i] + card[j] + card[k]
            if sum_value <= m:
                result = max(result, sum_value)
print(result)