'''
소트인사이드
'''

number = list(map(int, list(input())))

number.sort(reverse=True)

for i in number:
  print(i, end='')