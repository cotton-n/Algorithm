from collections import deque


def isOneDiff(word1, word2, wordLength):
    count = 0
    for i in range(wordLength):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = []
    wordLength = len(words)

    for i in range(wordLength):
        p


    return answer


if __name__ == '__main__':
    # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # 0
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
