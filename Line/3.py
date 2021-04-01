def solution(n):
  count = 0
  
  while n / 10 >= 1:
    flag = True
    strN = str(n)
    mid = len(strN) // 2
    while strN[mid:][0] == '0':
      mid += 1
      flag = False
    n = int(strN[mid:]) + int(strN[:mid])
    if flag:
      if len(strN) % 2 != 0:
        if strN[:mid + 1] > strN[mid:]:
          n = int(strN[mid:]) + int(strN[:mid])
        else:
          n = int(strN[mid+1:]) + int(strN[:mid+1])
      else:
        n = int(strN[mid:]) + int(strN[:mid])
    count += 1
  return [count, n]

print(solution(73425))
print(solution(52437))
print(solution(10007))
print(solution(19998997))
print(solution(9))