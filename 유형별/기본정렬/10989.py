'''
수 정렬하기3

계수 정렬(Counting Sort)
=> 데이터 개수는 많지만 범위가 좁을 때 사용하는 알고리즘
=> 범위 1 ~ 10,000 / 개수 10,000,000 
=> 시간 복잡도 O(N)

파이썬은 1초에 2천만개 연산 가능
데이터 개수가 많을 때는 sys.stdin.readline 사용
'''

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
  data = int(sys.stdin.readline())
  array[data] += 1
  
for i in range(10001):
  if array[i] != 0:
    for j in range(array[i]):
      print(i)