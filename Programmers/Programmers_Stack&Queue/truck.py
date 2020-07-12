import queue


def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = queue.Queue()
    truck = queue.Queue()

    for _ in range(bridge_length):
        q.put(0)

    for t in truck_weights:
        truck.put(t)

    total_weight = 0
    while q.queue:
        answer += 1
        total_weight -= q.get()
        if truck.queue:
            if total_weight + truck.queue[0] <= weight:
                w = truck.get()
                q.put(w)
                total_weight += w
            else:
                q.put(0)

    return answer


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
