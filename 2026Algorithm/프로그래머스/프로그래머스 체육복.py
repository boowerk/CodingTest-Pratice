# 여벌이 있으면서 도난도 당한 학생을 먼저 정리한 뒤 앞뒤 학생에게 빌려주는 그리디 풀이
def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 여벌이 있지만 도난당한 학생은 스스로 해결하므로 양쪽 집합에서 제거한다.
    both = lost_set & reserve_set
    lost_set -= both
    reserve_set -= both

    for student in sorted(lost_set):
        # 앞번호 학생부터 빌릴 수 있으면 먼저 사용하고, 없으면 뒷번호를 확인한다.
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
        else:
            n -= 1

    return n
