def solution(genres, plays):
    genre_total = {}
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre not in genre_total:
            genre_total[genre] = 0
            genre_songs[genre] = []

        genre_total[genre] += play
        genre_songs[genre].append((play, i))

    # 총 재생 수가 많은 장르 순서로 정렬
    sorted_genres = sorted(genre_total.keys(), key=lambda g: genre_total[g], reverse=True)

    answer = []

    for genre in sorted_genres:
        # 장르 안에서 재생 수 내림차순, 고유 번호 오름차순
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))

        # 최대 2곡 선택
        for play, idx in songs[:2]:
            answer.append(idx)

    return answer