'''
치즈
'''

import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())
array = []

for _ in range(h): 
  array.append(list(map(int, sys.stdin.readline().split())))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
remain = 0
count = 0
cheese = 0

for i in range(h):
  for j in range(w):
      if array[i][j] == 1:
          remain += 1
            
def delete():
  for i in range(h):
    for j in range(w):
      if array[i][j] == 2:
        array[i][j] = 0

while remain != 0:
  visited = [[0 for _ in range(w)] for _ in range(h)]
  queue.append([0, 0])
  visited[0][0] = 1
  if remain != 0: cheese = remain
  while queue:
    current = queue.popleft()
    for i in range(4):
      ndx = current[0] + dx[i]
      ndy = current[1] + dy[i]

      if 0 <= ndx < h and 0 <= ndy < w and visited[ndx][ndy] == 0:
        visited[ndx][ndy] = 1

        if array[ndx][ndy] == 1:
          array[ndx][ndy] = 2
          remain -= 1
        else:
          queue.append([ndx, ndy])
  count += 1
  delete()
        
print(count) 
print(cheese)
