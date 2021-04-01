'''
키로거
'''

from collections import deque

t = int(input())
 
for _ in range(t):
  inputStr = input()
  stack = [] 
  queue = deque()
  size = 0
  
  for s in inputStr:
    if s == '<':
      if len(stack) > 0:
        queue.appendleft(stack.pop())
    elif s == '>':
      if len(queue) > 0:
        stack.append(queue.popleft())
    elif s == '-':
      if len(stack) > 0:
        stack.pop() 
    else:
      stack.append(s)
  print(''.join(stack) + ''.join(queue))
