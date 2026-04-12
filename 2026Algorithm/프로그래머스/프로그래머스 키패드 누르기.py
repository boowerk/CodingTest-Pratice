def solution(numbers, hand):
    answer = []

    pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left = pos['*']
    right = pos['#']

    for num in numbers:
        if num in [1, 4, 7]:
            answer.append('L')
            left = pos[num]

        elif num in [3, 6, 9]:
            answer.append('R')
            right = pos[num]

        else:
            target = pos[num]
            left_dist = abs(left[0] - target[0]) + abs(left[1] - target[1])
            right_dist = abs(right[0] - target[0]) + abs(right[1] - target[1])

            if left_dist < right_dist:
                answer.append('L')
                left = target
            elif right_dist < left_dist:
                answer.append('R')
                right = target
            else:
                if hand == "left":
                    answer.append('L')
                    left = target
                else:
                    answer.append('R')
                    right = target

    return ''.join(answer)