"""
숫자 카드 게임
"""

n, m  = map(int, input().split())

result = 0

for _ in range(n):
    nums = list(map(int, input().split()))
    result = max(min(nums), result) # 메모리 효율

print(result)
