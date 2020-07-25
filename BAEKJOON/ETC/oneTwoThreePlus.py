def plus(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    else:
        return plus(x - 1) + plus(x - 2) + plus(x - 3)


n = int(input())
a = []
result = []

for _ in range(n):
    a.append(int(input()))

for val in a:
    print(plus(val))

