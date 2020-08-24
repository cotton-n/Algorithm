"""
큰 수의 법칙
"""

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

max_num = nums[-1]
max_num2 = nums[-2]
cal = max_num * k + max_num2

print(cal * (m // (k+1)) + max_num * (m % (k+1)))
