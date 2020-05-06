from collections import defaultdict
from operator import itemgetter


def solution(genres, plays):
    answer = []

    genre_rank = defaultdict(lambda: 0)

    for genre, play in zip(genres, plays):
        genre_rank[genre] += play

    genre_rank = sorted(genre_rank.items(), reverse=True, key=itemgetter(1))

    music_dic = defaultdict(lambda: [])

    for i, music_tuple in enumerate(zip(genres, plays)):
        music_dic[music_tuple[0]].append((music_tuple[1], i))

    for genre in genre_rank:
        one_music_dic = sorted(music_dic[genre[0]], reverse=True, key=itemgetter(0))
        # print(one_music_dic)
        answer.append(one_music_dic[0][1])
        if len(one_music_dic) > 1:
            answer.append(one_music_dic[1][1])

    return answer


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400, 600, 150, 2500, 500, 500]))
