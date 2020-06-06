def solution(heights):
    answer = []

    max_num = [-1, -1]

    for i, height in enumerate(heights):
        if max_num[0] <= height:
            max_num[0] = height
            max_num[1] = i
            answer.append(0)
        elif heights[i - 1] > height:
            answer.append(i)
        elif heights[answer[-1]-1] > height:  # 4번째 예외 잡음
            answer.append(answer[-1])
        else:
            answer.append(max_num[1] + 1)

    return answer


if __name__ == "__main__":
    print(solution([3, 6, 3, 3, 1, 2]))  # 4번째 테스트케이스에서 예외 [0, 0, 2, 2, 4, 4]
