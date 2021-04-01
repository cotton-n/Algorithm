def solution(dataSource, tags):
  answer = []
  document = {}
  
  for data in dataSource:
    document[data[0]] = 0
    for tag in tags: 
      if tag in data[1:]:
        document[data[0]] += 1
  sortData = sorted(document.items(), key=lambda x: (-x[1], x[0]))
  for data in sortData:
    if data[1] == 0: break
    answer.append(data[0])
  return answer

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"]
))