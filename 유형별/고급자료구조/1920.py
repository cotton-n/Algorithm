'''
수 찾기
'''

n = int(input())
A = map(int, input().split())
m = int(input())
search = map(int, input().split())

dicA = {}

for num in A:
  dicA[num] = 0
  
for s in search:
  try:
    dicA[s] += 1
    print(1)
  except KeyError:
    print(0)
