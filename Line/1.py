def solution(boxes):
  count = {}
  answer = len(boxes)
  
  for box in boxes:
    try:
      count[box[0]] += 1
    except KeyError:
      count[box[0]] = 1
    try:  
      count[box[1]] += 1
    except KeyError:
      count[box[1]] = 1
      
  for key, value in count.items():
    if value % 2 == 0:
      b = value // 2
      answer -= b
    if answer <= 0: break 
  
  if answer < 0: answer = 0
  return answer

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))