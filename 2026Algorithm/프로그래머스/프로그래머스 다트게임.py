# 문자열을 한 턴씩 읽어 점수를 계산하는 파싱 풀이
def solution(dartResult):
    scores = []
    i = 0

    while i < len(dartResult):
        # 10은 두 글자이므로 먼저 예외 처리한다.
        if dartResult[i] == '1' and i + 1 < len(dartResult) and dartResult[i + 1] == '0':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1

        bonus = dartResult[i]
        # 보너스에 따라 점수를 1제곱, 2제곱, 3제곱한다.
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
                # 스타상은 현재 점수와 바로 이전 점수를 함께 두 배로 만든다.
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
                i += 1
            elif dartResult[i] == '#':
                # 아차상은 현재 점수만 음수로 바꾼다.
                scores[-1] *= -1
                i += 1
    return sum(scores)
