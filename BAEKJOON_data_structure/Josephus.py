import sys

n, k = map(int, sys.stdin.readline().split())

p = []
size = n
for i in range(1, n+1):
    p.append(i)

index = k-1
answer = []
while size > 0:
    answer.append(p[index])
    del p[index]
    size -= 1
    if size > 0:
        if index + k <= size:
            index = index + k - 1
        else:
            index = index + k - size - 1
            while index >= size:
                index = index % size

string = '<'
for i, a in enumerate(answer):
    if i < n - 1:
        string = string + str(a) + ', '
    else:
        string = string + str(a)
string += '>'

print(string)
