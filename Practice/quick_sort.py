import random

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [item for item in data if item < pivot]
    right = [item for item in data if item > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    data_list = random.sample(range(100), 10)
    print(data_list)
    quick_list = quick_sort(data_list)
    print(quick_list)