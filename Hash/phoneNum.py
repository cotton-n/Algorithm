def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)-1):
        # print('i = ', phone_book[i])
        for j in range(i+1, len(phone_book)):
            # print('j = ', phone_book[j])
            # print(phone_book[j][0:len(phone_book[i])])
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                answer = False
                return answer

    return answer


if __name__ == "__main__":
    print(solution(	["119", "97674223", "1195524421"]))
