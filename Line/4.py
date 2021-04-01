def solution(maze):
    answer = 0
    size = len(maze)
    position = [0, 0]
    turn = 1
    if maze[0][1] == 1:
        turn = 2
    
    while position != [size - 1, size - 1]:
        if turn == 2:
            if position[1] + 1 == size or maze[position[0]][position[1] + 1] == 1:
                if position[0] + 1 == size or maze[position[0] + 1][position[1]] == 1:
                    turn = 3
                    continue
                position[0] += 1
            else:
                position[1] += 1
                turn = 1
        elif turn == 1:
            if position[0] == 0 or maze[position[0] - 1][position[1]] == 1:
                if position[1] + 1 == size or maze[position[0]][position[1] + 1] == 1:
                    turn = 2
                    continue
                position[1] += 1
            else:
                position[0] -= 1
                turn = 0 
        elif turn == 0:
            if position[1] == 0 or maze[position[0]][position[1] - 1] == 1:
                if position[0] == 0 or maze[position[0] - 1][position[1]] == 1:
                    turn = 1
                    continue
                position[0] -= 1
            else:
                position[1] -= 1
                turn = 3
        else:
            if position[0] + 1 == size or maze[position[0] + 1][position[1]] == 1:
                if position[1] == 0 or maze[position[0]][position[1] - 1] == 1:
                    turn = 0
                    continue
                position[1] -= 1
            else:
                position[0] += 1
                turn = 2 
        answer += 1
    
    return answer

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))