"""
더하기 사이클
"""

from sys import stdin

n = stdin.readline().rstrip()
new_n = n
count = 0

while True:
    if len(new_n) == 1:
        new_n = '0' + new_n
    s = int(new_n[0]) + int(new_n[1])
    string = str(s)
    new_n = new_n[1] + string[-1]
    count += 1
    if int(new_n) == int(n):
        break

print(count)
