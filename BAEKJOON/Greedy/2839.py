"""
설탕 배달 - 보류
"""

n = int(input())

result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        break
    if n < 5 and n % 3 != 0:
        result = -1
        break
    n -= 3
    result += 1
    
print(result)
