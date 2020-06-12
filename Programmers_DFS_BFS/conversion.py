from collections import deque


# 한 글자만 다른지 판단하는 함수
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
    queue = deque()  # deque 이용
    queue.append([begin, 0])  # (단어, 변환횟수)
    while queue:
        w, c = queue.popleft()
        if w == target:
            answer = c
            break
        for word in words:
            if isOneDiff(w, word, wordLength):
                # 한글자만 다를 때
                queue.append([word, c+1])
                words.remove(word)
    return answer


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))    # 0
