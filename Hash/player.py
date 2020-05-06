def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion):
        if i != j:
            return i
    return participant[-1]


if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["kiki", "eden"]))
