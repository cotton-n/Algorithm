from sys import stdin


def solution(friends, user_id):
    answer = []
 
    user_friends = []
    other_friends = {}
    mutual_friend = {}

    for friend in friends:
         # user_id의 친구 목록
        if friend[0] == user_id:
            user_friends.append(friend[1])
        elif friend[1] == user_id:
            user_friends.append(friend[0])
         # 친구가 아닌 애들의 친구 목록
        else:
            try:
                other_friends[friend[0]].append(friend[1])
            except KeyError:
                other_friends[friend[0]] = [friend[1]]
            try:
                other_friends[friend[1]].append(friend[0])
            except KeyError:
                other_friends[friend[1]] = [friend[0]]


    # 친구 제외
    for friend in user_friends:
        del other_friends[friend]

    # 비교를 해서 count 
    for key, value in other_friends.items():
        for friend in user_friends:
            if friend in value:
                try:
                    mutual_friend[key] += 1
                except KeyError:
                    mutual_friend[key] = 1
        
    sorted(mutual_friend.items(), key = lambda item: item[1])
    
    # 가장 count가 큰 친구를 추천
    prev_count = -1
    flag = False
    for key, value in mutual_friend.items():
        if flag and (prev_count != value):
            break
        answer.append(key)
        prev_count = value
        flag = True

    return answer


if __name__ == '__main__':
    print(solution([["david", "frank"], ["demi", "david"], ["frank", "james"], ["demi", "james"], ["claire", "frank"]], "david")) 
    # ["james"]
    print(solution([["david", "demi"], ["frank", "demi"], ["demi", "james"]], "frank")) 
    # ["david", "james"]