'''
친구 네트워크(나중에 다시 풀어보기)
union-find 알고리즘 활용
'''

def find(x):
  if x == parent[x]:
    return x
  else:
    p = find(parent[x])
    parent[x] = p
    return p

def union(x, y):
  x = find(x)
  y = find(y)
  
  if x != y:
    parent[y] = x
    number[x] += number[y]
    
t = int(input())

for _ in range(t):
  parent = dict()
  number = dict()
  
  f = int(input())
  
  for _ in range(f):
    x, y = input().split()
    
    if x not in parent:
      parent[x] = x
      number[x] = 1
    if y not in parent:
      parent[y] = y
      number[y] = 1
      
    union(x, y)
    print(number[find(x)])
      