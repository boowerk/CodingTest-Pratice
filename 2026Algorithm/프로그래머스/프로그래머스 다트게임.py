def solution(dartResult):
    scores = []
    i = 0

    while i < len(dartResult):
        if dartResult[i] == '1' and i + 1 < len(dartResult) and dartResult[i + 1] == '0':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1

        bonus = dartResult[i]
        if bonus == 'S':
            num = num ** 1
        elif bonus == 'D':
            num = num ** 2
        elif bonus == 'T':
            num = num ** 3
        i += 1

        scores.append(num)

        if i < len(dartResult):
            if dartResult[i] == '*':
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
                i += 1
            elif dartResult[i] == '#':
                scores[-1] *= -1
                i += 1
    return sum(scores)