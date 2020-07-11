import random

def merge_split(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_split(data[:mid])
    right = merge_split(data[mid:])
    return merge(left, right)

def merge(left, right):
    left_index, right_index = 0, 0
    result = list()
    # left, rght 둘다 남아있을 때
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # left만 남아있을 때
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    # right만 남아있을 때
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result

if __name__ == "__main__":
    data_list = random.sample(range(100), 10)
    print(data_list)
    merge_list = merge_split(data_list)
    print(merge_list)