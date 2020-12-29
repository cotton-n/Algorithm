"""
왕실의 나이트
"""

position = list(input())
move = [[1, 2], [1, -2], [-1, 2], [-1, -2], [-2, -1], [-2, 1], [2, -1], [2, 1]]
alpha = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h':8
}

knight = [alpha[position[0]], int(position[1])]
count = 0

for m in move:
    if 0 < knight[0] + m[0] <= 8 and 0 < knight[1] + m[1] <= 8:
        count += 1

print(count)
