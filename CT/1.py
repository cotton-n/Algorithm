def solution(n):
    num = n + 1

    while True:
        b = False
        st = str(num)
        dic = {}
        for s in st:
            try:
                dic[s] += 1
                b = True
                break
            except KeyError:
                dic[s] = 1

        if b:
            num += 1
        else:
            break

    return num


if __name__ == '__main__':
    print(solution(1987))
    print(solution(2015))
