def solution(road, n):
  answer = -1
  road_list = road.split('0')
  road_list = [len(road) for road in road_list]
  
  if n >= len(road_list):
      sum = 0
      
      for i in road_list:
          sum += i
      answer = sum + len(road_list) - 1
      
  else:
      for i in range(len(road_list) - n):
          sum = 0

          for j in range(n+1):
              sum += road_list[i+j]

          answer = sum+n if sum+n > answer else answer
      
  return answer


print(solution('111011110011111011111100011111', 3))
print(solution('001100', 5))