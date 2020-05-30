def solution(numbers, target):
    answer = 0
    length = len(numbers)

    def operator(total, idx):
        if idx < length:
            numbers[idx] *= 1
            operator(total+numbers[idx], idx+1)

            numbers[idx] *= -1
            operator(total + numbers[idx], idx + 1)

        elif total == target:
            nonlocal answer
            answer += 1

    operator(0, 0)

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
