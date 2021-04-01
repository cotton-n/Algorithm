'''
0 만들기(나중에 다시 풀어보기)
테스트 케이스가 적고 자연수 범위도 작기 때문에 완전탐색 활용
'''

import copy

def recursive(array, n):
  if len(array) == n:
    operators_list.append(copy.deepcopy(array))
    return
  array.append(' ')
  recursive(array, n)
  array.pop()
  array.append('+')
  recursive(array, n)
  array.pop()
  array.append('-')
  recursive(array, n)
  array.pop()
  
t = int(input())

for _ in range(t):
  operators_list = []
  n = int(input())
  recursive([], n - 1)
  integers = [i for i in range(1, n + 1)]
  
  for operators in operators_list:
    string = ''
    for i in range(n - 1):
      string += str(integers[i]) + operators[i]
    string += str(integers[-1])
    if eval(string.replace(' ', '')) == 0:
      print(string)
  print()
  