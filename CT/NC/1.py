def solution(compressed):
    answer = ""
    temp = []
    stack = []
    s = ""
    size = 0
    flag = False
    for comp in compressed:
        if comp.isdigit():
            if temp and temp[-1].isdigit():
                temp.append(temp.pop() + comp)
                size += 1
            else:
                temp.append(comp)
                size += 1
        elif comp == '(':
            temp.append(comp)
            size += 1
            flag = True
        elif comp == ')':
            if s != "":
                temp.append(s)
            temp.append(comp)
            size += 2
            flag = False
            s = ""
        else:
            if flag:
                s += comp
            else:
                temp.append(comp)
                size += 1
    print(temp)
    s = ""
    while len(temp) != 1:
        a = temp.pop()
        if a == ')':
            s = temp.pop()
        elif a == '(':
            n = temp.pop()
            temp.append(s * int(n))
        else:
            x = temp.pop()
            temp.append(x+a)
        print(temp)
    return answer


if __name__ == '__main__':
    print(solution("2(2(hi)2(co))x2(bo)"))
