"""
쿼드 트리
"""

from sys import stdin

n = int(stdin.readline().rstrip())
quad_tree = list()
for _ in range(n):
    quad_tree.append(list(stdin.readline().rstrip()))

def check(tree):
    a = tree[0][0]
    for t in tree:
        for n in t:
            if a != n:
                return False
    return True

def merge_split(tree):
    if check(tree):
        return tree[0][0]
    medium = len(tree) // 2

    left_top = list()
    right_top = list()
    left_down = list()
    right_down = list()
    for t in tree[:medium]:
        left_top.append(t[:medium])
        right_top.append(t[medium:])
    for t in tree[medium:]:
        left_down.append(t[:medium])
        right_down.append(t[medium:])

    left_top = merge_split(left_top)
    right_top = merge_split(right_top)
    left_down = merge_split(left_down)
    right_down = merge_split(right_down)

    return merge(left_top, right_top, left_down, right_down)

def merge(left_top, right_top, left_down, right_down):
    return f'({left_top}{right_top}{left_down}{right_down})' 

print(merge_split(quad_tree))
