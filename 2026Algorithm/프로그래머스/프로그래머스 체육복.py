def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    both = lost_set & reserve_set
    lost_set -= both
    reserve_set -= both

    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
        else:
            n -= 1

    return n