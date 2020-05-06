import sys

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

numDic = {}
dic = {}

for i, li in enumerate(a):
    numDic[i+1] = li[0]
    dic[i+1] = li[1:]

for key, value in dic.items():
    #print(key, numDic[key])
    #print(key, value)
    if len(value) != 1:
        print(key, value)
        i = 0
        while value[i] != -1:
            # dic[key].append()
            i += 1

# for i, li in enumerate(a):
#     s = li[0]
#     while len(li) >= 3:
#         s += dic[li[1]]
#         del li[1]
#     if len(li) == 2:
#         print(s)
