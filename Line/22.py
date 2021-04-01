from itertools import combinations

def solution(answer_sheet, sheets):
  answer = 0
  
  people = [i for i in range(len(sheets))]
  
  for p in combinations(people, 2):
    count = 0
    continuity = 0
    temp = 0
    for i, a in enumerate(answer_sheet):
      if sheets[p[0]][i] == sheets[p[1]][i] and sheets[p[1]][i] != a:
        count += 1
        temp += 1
      else:
        continuity = max(temp, continuity)
        temp = 0
    continuity = max(temp, continuity)
    answer = max(answer, count + continuity ** 2)
  
  return answer

print(solution('4132315142', ["3241523133","4121314445","3243523133","4433325251","2412313253"]))
print(solution('53241', ["53241", "42133", "53241", "14354"]))
print(solution('24551', ["24553", "24553", "24553", "24553"]))