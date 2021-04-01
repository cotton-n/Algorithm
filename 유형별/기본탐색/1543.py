'''
문서 검색
'''

string = input()
target = input()
answer = 0

while target in string:
  string = string[string.find(target)+len(target):]
  answer += 1
  
print(answer)

# document = input()
# word = input()
# index = 0
# result = 0
# while len(document) - index >= len(word):
#   if document[index:index + len(word)] == word:
#     result += 1
#     index += len(word)
#   else:
#     index += 1
# print(result)
