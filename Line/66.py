def solution(directory, command):
  answer = directory

  for c in  command:
    cList = c.split()
    if cList[0] == 'mkdir':
      answer.append(cList[1])
    elif cList[0] == 'rm':
      matching = [s for s in answer if cList[1] in s] 
      for m in matching:
        answer.remove(m) 
    elif cList[0] == 'cp':
      matching = [s for s in answer if cList[1] in s] 
      answer.append(cList[2] + cList[1].split('/')[-1])
      for m in matching:
        if m != cList[1]: 
          answer.append(cList[2] + cList[1].split('/')[-1] + m.split(cList[1].split('/')[-1])[-1])
  
  answer.sort()
  return answer

print(solution([
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
], [
"mkdir /root/tmp",
"cp /hello /root/tmp", 
"rm /hello"
]))

print(solution([
"/"
], [
"mkdir /a",
"mkdir /a/b",
"mkdir /a/b/c",
"cp /a/b /",
"rm /a/b/c"
]))