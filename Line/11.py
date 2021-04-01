def solution(inputString):
  answer = 0
  
  bracket = {')' : '(', '}' : '{', ']' : '[', '>' : '<'}
  count = {'(' : 0, '{' : 0, '[' : 0, '<' : 0}
  
  for s in inputString:
    if s == '(' or s == '{' or s == '[' or s == '<':
      count[s] += 1
    elif  s == ')' or s == '}' or s == ']' or s == '>':
      if count[bracket[s]] == 0:
        answer = -1
        break
      else:
        count[bracket[s]] -= 1
        answer += 1
  
  return answer

print(solution('Hello, world!'))
print(solution('line [plus]'))
print(solution('if (Count of eggs is 4.) {Buy milk}'))
print(solution('>_<'))