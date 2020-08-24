"""
로프
"""

n = int(input())
ropes = list()

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()
max_weight = 0
i = 0
for rope in ropes:
    max_weight = max(rope * (n - i), max_weight)
    i += 1

print(max_weight)
