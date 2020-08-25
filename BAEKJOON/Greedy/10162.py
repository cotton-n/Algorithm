"""
전자레인지
"""

t = int(input())

buttons = [300, 60, 10]

result = list()
for button in buttons:
    result.append(t // button) 
    t %= button

if t != 0:
    print(-1)
else:
    for r in result:
        print(r, end=' ')
