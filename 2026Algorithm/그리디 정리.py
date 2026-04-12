# =========================================================
# 🔥 GREEDY 통합 템플릿 (시험장용)
# =========================================================
# ✔ 정렬 → 선택 → 조건 → 반복
# ✔ 필요한 부분만 골라서 사용
# ✔ 프로그래머스 1~3레벨 대부분 커버 가능
# =========================================================

from collections import deque


# ---------------------------------------------------------
# 1. 기본 그리디 구조
# ---------------------------------------------------------
def greedy_basic(arr, limit):
    """
    ✔ 가장 기본적인 그리디 패턴
    ✔ 누적하면서 조건 만족하는 만큼 선택
    """

    arr.sort()  # 필요에 따라 reverse=True

    current = 0
    count = 0

    for x in arr:
        if current + x <= limit:
            current += x
            count += 1
        else:
            break

    return count


# ---------------------------------------------------------
# 2. 동전 문제 (거스름돈)
# ---------------------------------------------------------
def coin_change(n, coins):
    """
    ✔ 최소 동전 개수
    ✔ 큰 단위부터 선택
    """

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        count += n // coin
        n %= coin

    return count


# ---------------------------------------------------------
# 3. 회의실 배정 (활동 선택)
# ---------------------------------------------------------
def meeting_schedule(meetings):
    """
    ✔ 최대 회의 개수
    ✔ 종료 시간 기준 정렬
    """

    meetings.sort(key=lambda x: (x[1], x[0]))

    end_time = 0
    count = 0

    for start, end in meetings:
        if start >= end_time:
            count += 1
            end_time = end

    return count


# ---------------------------------------------------------
# 4. 큰 수 만들기 (스택 기반 그리디)
# ---------------------------------------------------------
def make_big_number(number, k):
    """
    ✔ 숫자 제거해서 최대값 만들기
    ✔ 스택 사용
    """

    stack = []

    for num in number:
        # 더 큰 수를 만들기 위해 이전 작은 값 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)

    # 아직 제거 못한 경우 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


# ---------------------------------------------------------
# 5. 체육복 문제
# ---------------------------------------------------------
def gym_uniform(n, lost, reserve):
    """
    ✔ 앞뒤 학생에게만 빌려줄 수 있음
    ✔ 집합 활용 핵심
    """

    lost = set(lost) - set(reserve)
    reserve = set(reserve) - set(lost)

    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)


# ---------------------------------------------------------
# 6. 모험가 길드
# ---------------------------------------------------------
def adventurer_guild(fears):
    """
    ✔ 공포도 기준 그룹 생성
    """

    fears.sort()

    group = 0
    result = 0

    for fear in fears:
        group += 1

        if group >= fear:
            result += 1
            group = 0

    return result


# ---------------------------------------------------------
# 7. 문자열 뒤집기 (최소 횟수)
# ---------------------------------------------------------
def flip_string(s):
    """
    ✔ 0과 1 그룹 개수 세기
    ✔ 최소값 반환
    """

    count0 = 0
    count1 = 0

    # 첫 문자 기준
    if s[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            if s[i] == '1':
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)


# ---------------------------------------------------------
# 8. 최소 / 최대 선택 패턴
# ---------------------------------------------------------
def min_sum(arr, k):
    """가장 작은 k개 합"""
    arr.sort()
    return sum(arr[:k])


def max_sum(arr, k):
    """가장 큰 k개 합"""
    arr.sort(reverse=True)
    return sum(arr[:k])


# ---------------------------------------------------------
# 9. 그리디 판단용 헬퍼
# ---------------------------------------------------------
def greedy_template(arr):
    """
    ✔ 시험장에서 빠르게 쓰는 템플릿
    ✔ 조건만 바꿔서 사용
    """

    # 1. 정렬 (문제에 따라 바꿔라)
    arr.sort()  # or reverse=True

    answer = 0
    current = 0

    for x in arr:
        # 2. 조건 체크 (여기 수정!)
        if current + x <= 100:   # ← 문제 조건으로 바꿔라
            current += x
            answer += 1
        else:
            break

    return answer


# ---------------------------------------------------------
# 10. 메인 solution 구조 (시험용)
# ---------------------------------------------------------
def solution(data):
    """
    ✔ 실제 시험에서 사용하는 기본 구조
    ✔ 문제에 맞게 아래 코드 수정해서 사용
    """

    # ---------------------------------------------
    # 예시: 기본 그리디 사용
    # ---------------------------------------------
    arr = data

    # 정렬 방식 선택
    arr.sort()  # or reverse=True

    answer = 0
    current = 0

    for x in arr:
        # 문제 조건에 맞게 수정
        if current + x <= 100:
            current += x
            answer += 1

    return answer


# ---------------------------------------------------------
# 11. 테스트 코드
# ---------------------------------------------------------
if __name__ == "__main__":
    print("기본:", greedy_basic([1,2,3,4,5], 7))
    print("동전:", coin_change(1260, [500,100,50,10]))
    print("회의:", meeting_schedule([(1,4),(2,3),(3,5)]))
    print("큰수:", make_big_number("1924", 2))
    print("체육복:", gym_uniform(5, [2,4], [1,3,5]))
    print("모험가:", adventurer_guild([2,3,1,2,2]))
    print("문자열:", flip_string("0001100"))