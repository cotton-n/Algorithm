from collections import Counter


def solution(clothes):
    counter_each_category = Counter([cat for _, cat in clothes])
    print([cat for _, cat in clothes])  # ['headgear', 'eyewear', 'headgear']
    print(counter_each_category)  # Counter({'headgear': 2, 'eyewear': 1})

    all_possible = 1

    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)  # +1 : 안입는 경우를 더한 것

    return all_possible - 1  # -1 : 다 안입는 경우를 뺀 것


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
