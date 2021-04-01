'''
수 정렬하기2

데이터 개수 1,000,000
O(NlogN) 정렬 알고리즘 이용 -> 병합 정렬, 퀵 정렬, 힙 정렬 등
파이썬 기본 정렬 라이브러리도 가능

메모리가 허용된다면 Python3보다 PyPy3 선택
'''

import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
  data.append(int(sys.stdin.readline()))

data.sort()

for d in data:
  print(d)
