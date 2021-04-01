'''
좌표 정렬하기
'''

n = int(input())
coordinate = []

for _ in range(n):
  coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x: (x[0], x[1]))

for c in coordinate:
  print(c[0], c[1])
