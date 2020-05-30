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
    answer = 0
    wordLength = len(begin)
    queue = deque()
    queue.append([begin, 0])
    while queue:
        w, c = queue.popleft()
        if w == target:
            answer = c
            break
        for word in words:
            if isOneDiff(w, word, wordLength):
                queue.append([word, c+1])
                words.remove(word)
    return answer


if __name__ == '__main__':
    # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # 0
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
