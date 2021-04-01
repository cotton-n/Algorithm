'''
프린터 큐
'''

from collections import deque

n = int(input())

for _ in range(n):
  m, target = map(int, input().split())
  temp = list(map(int, input().split()))
  queue = deque([(i, value) for i, value in enumerate(temp)])
  temp.sort(reverse=True)
  queueTemp = deque(temp)
  answer = 0
  while queue:
    popData = queue.popleft()
    if popData[1] == queueTemp[0]:
      queueTemp.popleft()
      answer += 1
      if popData[0] == target:
        break
    else:
      queue.append(popData)
  print(answer)
