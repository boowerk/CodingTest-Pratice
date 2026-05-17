# ============================================================
# 실전용 Python 이진 탐색 정리
# 핵심 조건:
# 1. 배열이 정렬되어 있어야 함
# 2. 탐색 범위를 left, right로 줄여나감
# 3. 보통 O(log N)
# ============================================================

from bisect import bisect_left, bisect_right


# ============================================================
# 1. 기본 이진 탐색
# 정렬된 배열에서 target이 존재하는지 확인
# 있으면 인덱스 반환, 없으면 -1 반환
# ============================================================
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ============================================================
# 2. lower_bound
# target 이상이 처음 나오는 위치
# Python bisect_left와 같음
# ============================================================
def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================================
# 3. upper_bound
# target보다 큰 값이 처음 나오는 위치
# Python bisect_right와 같음
# ============================================================
def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================================
# 4. 특정 값의 개수 구하기
# 정렬된 배열에서 target의 개수
# ============================================================
def count_target(arr, target):
    left = lower_bound(arr, target)
    right = upper_bound(arr, target)

    return right - left


# ============================================================
# 5. bisect 사용 버전
# 실전에서는 직접 구현보다 이걸 더 자주 사용
# ============================================================
def count_target_with_bisect(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)

    return right - left


# ============================================================
# 6. 범위 안에 있는 값의 개수
# 예: left_value <= x <= right_value 인 원소 개수
# ============================================================
def count_range(arr, left_value, right_value):
    left = bisect_left(arr, left_value)
    right = bisect_right(arr, right_value)

    return right - left


# ============================================================
# 7. 파라메트릭 서치 기본 형태
# 조건을 만족하는 최소값 찾기
#
# 예시:
# check(mid)가 True면 답이 될 수 있으므로 더 작은 쪽 탐색
# check(mid)가 False면 더 큰 쪽 탐색
# ============================================================
def parametric_search_min(left, right, check):
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


# ============================================================
# 8. 파라메트릭 서치 기본 형태
# 조건을 만족하는 최대값 찾기
#
# check(mid)가 True면 답이 될 수 있으므로 더 큰 쪽 탐색
# check(mid)가 False면 더 작은 쪽 탐색
# ============================================================
def parametric_search_max(left, right, check):
    answer = left

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


# ============================================================
# 9. 실전 예제 1
# 백준 1920 수 찾기 유형
# ============================================================
def example_find_number():
    arr = [4, 1, 5, 2, 3]
    targets = [1, 3, 7, 9, 5]

    arr.sort()

    for target in targets:
        if binary_search(arr, target) != -1:
            print(1)
        else:
            print(0)


# ============================================================
# 10. 실전 예제 2
# 백준 10816 숫자 카드 2 유형
# 특정 숫자가 몇 개 있는지 구하기
# ============================================================
def example_count_number():
    arr = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
    targets = [10, 9, -5, 2, 3, 4, 5, -10]

    arr.sort()

    for target in targets:
        print(count_target_with_bisect(arr, target), end=" ")


# ============================================================
# 11. 실전 예제 3
# 백준 2805 나무 자르기 유형
# 절단기 높이의 최댓값 구하기
# ============================================================
def example_tree_cut():
    trees = [20, 15, 10, 17]
    need = 7

    left = 0
    right = max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid

        # 가져갈 수 있는 나무가 충분함
        # 높이를 더 올려도 되는지 확인
        if total >= need:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


# ============================================================
# 12. 실전 예제 4
# 백준 1654 랜선 자르기 유형
# 만들 수 있는 랜선 길이의 최댓값 구하기
# ============================================================
def example_lan_cable():
    cables = [802, 743, 457, 539]
    need = 11

    left = 1
    right = max(cables)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for cable in cables:
            count += cable // mid

        # 필요한 개수 이상 만들 수 있음
        # 길이를 더 길게 해본다
        if count >= need:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


# ============================================================
# 13. 실전 예제 5
# 백준 2110 공유기 설치 유형
# 가장 인접한 공유기 사이 거리의 최댓값 구하기
# ============================================================
def example_router():
    houses = [1, 2, 8, 4, 9]
    router_count = 3

    houses.sort()

    left = 1
    right = houses[-1] - houses[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        installed = 1
        last_position = houses[0]

        for i in range(1, len(houses)):
            if houses[i] - last_position >= mid:
                installed += 1
                last_position = houses[i]

        # mid 거리 이상으로 공유기를 설치할 수 있음
        # 거리를 더 늘려본다
        if installed >= router_count:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


# ============================================================
# 실행 예시
# ============================================================
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]

    print("기본 이진 탐색:", binary_search(arr, 3))
    print("lower_bound:", lower_bound(arr, 2))
    print("upper_bound:", upper_bound(arr, 2))
    print("2의 개수:", count_target(arr, 2))
    print("2의 개수 bisect:", count_target_with_bisect(arr, 2))
    print("2 이상 4 이하 개수:", count_range(arr, 2, 4))

    print()
    print("수 찾기 예제")
    example_find_number()

    print()
    print("숫자 카드 2 예제")
    example_count_number()

    print()
    print()
    print("나무 자르기 예제")
    example_tree_cut()

    print()
    print("랜선 자르기 예제")
    example_lan_cable()

    print()
    print("공유기 설치 예제")
    example_router()


# ============================================================
# 시험용 요약
# ============================================================
# 1. 기본 이진 탐색
# while left <= right:
#     mid = (left + right) // 2
#
# 2. 값 존재 확인
# binary_search(arr, target) != -1
#
# 3. lower_bound
# bisect_left(arr, target)
# target 이상이 처음 나오는 위치
#
# 4. upper_bound
# bisect_right(arr, target)
# target보다 큰 값이 처음 나오는 위치
#
# 5. 특정 값 개수
# bisect_right(arr, x) - bisect_left(arr, x)
#
# 6. 범위 개수
# bisect_right(arr, right_value) - bisect_left(arr, left_value)
#
# 7. 최댓값 찾는 파라메트릭 서치
# 조건 만족하면:
#     answer = mid
#     left = mid + 1
#
# 8. 최솟값 찾는 파라메트릭 서치
# 조건 만족하면:
#     answer = mid
#     right = mid - 1
# ============================================================