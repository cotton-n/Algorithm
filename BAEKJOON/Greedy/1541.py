"""
잃어버린 괄호
"""

string = input()
arr = list()

num = ''
for s in string:
    if s.isdigit():
        num += s
    else:
        arr.append(int(num))
        num = ''
        arr.append(s)
arr.append(int(num))

last = list()
i = 0
while len(arr) != i:
    if arr[i] == '+':
        last.append(last.pop() + arr[i+1])
        i += 2
    else:
        last.append(arr[i])
        i += 1
i = 0
arr.clear()
while len(last) != i:
    if last[i] == '-':
        arr.append(arr.pop() - last[i+1])
        i += 2
    else:
        arr.append(last[i])
        i += 1

print(arr[0])

# 55-50+40+20-30
# -85
