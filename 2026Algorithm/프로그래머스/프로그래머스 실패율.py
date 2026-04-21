def solution(N, stages):
    count = [0] * (N + 2)

    for s in stages:
        count[s] += 1

    answer = []
    players = len(stages)

    for stages in range(1, N + 1):
        if players == 0:
            fail = 0
        else:
            fail = count[stages] / players

        answer.append((stages, fail))
        players -= count[stages]

    answer.sort(key=lambda x: (-x[1], x[0]))

    return [stage for stage, fail in answer]