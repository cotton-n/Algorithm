def solution(total_sp, skills):
    answer = []
    dic = {}
    result = {}
    i = 0
    for skill in skills:
        dic[skill[1]] = []
        dic[skill[1]].append(skill[0])
    for key, value in dic.items():
        print(key, value)

    return answer


if __name__ == '__main__':
    print(solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))
