"""
벌집
"""

from sys import stdin

n = int(stdin.readline().rstrip())

visited = []
queue = []

def bfs(current, goal):
    if current == goal:
        return 1
    if current > goal:
        return 0
    
    