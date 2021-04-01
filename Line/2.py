def solution(ball, order):
  answer = []
  priority = []
  index = 0
  
  while ball:
    if ball[0] == order[index]:
      ball = ball[1:]
      answer.append(order[index])
      if ball:
        while ball[0] in priority:
          priority.remove(ball[0])
          answer.append(ball[0])
          ball = ball[1:]
    elif ball[-1] == order[index]:
      ball = ball[:-1]
      answer.append(order[index])
      if ball:
        while ball[-1] in priority:
          priority.remove(ball[-1])
          answer.append(ball[-1])
          ball = ball[:-1]
    else:
      priority.append(order[index])
    index += 1
  return answer

print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))