import sys
import time

string = sys.stdin.readline()
n = int(sys.stdin.readline())
startTime = time.time()
stringArray = list(string)
del stringArray[-1]
# 커서의 위치 처음은 맨 마지막
start = 0
end = len(stringArray)
cur = end
strArray = stringArray
for i in range(n):
    op = sys.stdin.readline().split()
    if op[0] == 'P':
        word = op[1]
        strArray = strArray[:cur] + list(word) + strArray[cur:]
        cur += 1
    else:
        if op[0] == 'L':
            cur -= 1
            if cur < start:
                cur = start
            continue
        if op[0] == 'D':
            cur += 1
            if cur > end:
                cur = end
            continue
        if op[0] == 'B' and cur != 0:
            strArray = strArray[:cur-1] + strArray[cur:]
            cur -= 1
            continue

print(''.join(strArray))
print(time.time() - startTime)