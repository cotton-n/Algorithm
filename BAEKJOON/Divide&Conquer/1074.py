"""
Z
"""

from sys import stdin

n, r, c = map(int, stdin.readline().rstrip().split())

a = 0
x = 2 ** n
while x != 1:
    x //= 2
    if r < x and c >= x:
        a += (x * x)
        c -= x
    elif r >= x and c < x:
        a += (2 * x * x)
        r -= x
    elif r >= x and c >= x:
        a += (3 * x * x)
        r -= x
        c -= x 
print(a)


"""
아래는 분할정복 이용
근데 시간초과 발생
"""

# a = 0

# def merge_split(data):
#     global a
#     if data == 2:
#         data_list = [[a, a + 1], [a + 2, a + 3]]
#         a += 4
#         return data_list

#     medium = data // 2

#     left_top = merge_split(medium)
#     right_top = merge_split(medium)
#     left_down = merge_split(medium)
#     right_down = merge_split(medium)

#     return merge(left_top, right_top, left_down, right_down)

# def merge(left_top, right_top, left_down, right_down):
#     result = list()
#     size = len(left_top)
#     for i in range(size):
#         result.append(left_top[i] + right_top[i])
#     for i in range(size):
#         result.append(left_down[i] + right_down[i])

#     return result

# print(merge_split(2**n)[r][c])
