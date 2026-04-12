# 자주 나오는 그리디 풀이 패턴을 예제와 함께 모아둔 파일

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
        # 지금 선택해도 제한을 넘지 않으면 바로 채택한다.
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
        # 큰 단위 동전부터 최대한 많이 사용한다.
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
        # 현재 회의가 직전 회의 종료 시간 이후라면 선택 가능하다.
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
# 7. 만들 수 없는 금액
# ---------------------------------------------------------
def cannot_make_amount(coins):
    """
    ✔ 정렬 후 target을 유지하며
    ✔ 현재까지 만들 수 있는 연속 구간을 넓혀 가는 패턴
    """

    coins.sort()
    target = 1

    for coin in coins:
        # target보다 큰 동전이 나오면 target 금액은 만들 수 없다.
        if coin > target:
            break

        target += coin

    return target


# ---------------------------------------------------------
# 8. 구명보트 / 두 포인터 그리디
# ---------------------------------------------------------
def lifeboat(people, limit):
    """
    ✔ 가장 가벼운 사람과 가장 무거운 사람을 함께 태울 수 있는지 확인
    ✔ 안 되면 무거운 사람부터 혼자 보낸다
    """

    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


# ---------------------------------------------------------
# 9. 문자열 뒤집기 (최소 횟수)
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
# 10. 최소 / 최대 선택 패턴
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
# 11. 구간 덮기 템플릿
# ---------------------------------------------------------
def min_cover_segments(segments, start, end):
    """
    ✔ [start, end] 구간을 최소 개수의 구간으로 덮는 패턴
    ✔ 현재 덮인 지점까지 시작점이 들어오는 구간 중 가장 멀리 뻗는 구간 선택
    """

    segments.sort()
    idx = 0
    count = 0
    current = start

    while current < end:
        best = current

        while idx < len(segments) and segments[idx][0] <= current:
            best = max(best, segments[idx][1])
            idx += 1

        # 더 멀리 뻗는 구간이 하나도 없으면 덮기 실패다.
        if best == current:
            return -1

        current = best
        count += 1

    return count


# ---------------------------------------------------------
# 12. 그리디 판단용 헬퍼
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
# 13. 메인 solution 구조 (시험용)
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
# 14. 테스트 코드
# ---------------------------------------------------------
if __name__ == "__main__":
    print("기본:", greedy_basic([1,2,3,4,5], 7))
    print("동전:", coin_change(1260, [500,100,50,10]))
    print("회의:", meeting_schedule([(1,4),(2,3),(3,5)]))
    print("큰수:", make_big_number("1924", 2))
    print("체육복:", gym_uniform(5, [2,4], [1,3,5]))
    print("모험가:", adventurer_guild([2,3,1,2,2]))
    print("못만드는금액:", cannot_make_amount([3,2,1,1,9]))
    print("구명보트:", lifeboat([70, 50, 80, 50], 100))
    print("문자열:", flip_string("0001100"))
    print("구간덮기:", min_cover_segments([(1,4), (2,5), (4,7), (6,8)], 1, 8))
