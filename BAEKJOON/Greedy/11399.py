"""
ATM
"""

n = int(input())
p_time = list(map(int, input().split()))

p_time.sort()

result = 0
prev = 0
for time in p_time:
    result += (prev + time)
    prev += time

print(result)
