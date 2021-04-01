'''
새
'''

n = int(input())
k = 1
count = 0

while n > 0:
  if n - k < 0:
    k = 1
  n -= k
  k += 1
  count += 1
  
print(count)
