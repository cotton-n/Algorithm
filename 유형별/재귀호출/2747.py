'''
피보나치 수
'''

import sys

n = int(sys.stdin.readline())

fibo = [0] * 46

for i in range(46):
  if i < 2:
    fibo[i] = i
  else:
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])