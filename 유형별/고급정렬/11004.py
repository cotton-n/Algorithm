'''
K 번째 수
O(NlogN) 정렬 알고리즘 이용
'''

import sys

n, k = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))

numList.sort()

print(numList[k - 1])
