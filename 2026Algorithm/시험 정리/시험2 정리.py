# ============================================================
# 정렬 / 이진탐색 / 다이나믹 프로그래밍 실전 문제 정리
# Python 기준
#
# 사용법:
# - 백준에 제출할 때는 필요한 solve_xxx() 함수 하나만 남기고
#   맨 아래에서 해당 함수만 호출하면 됨
# - 프로그래머스 문제는 solution_xxx() 함수 형태로 사용
# ============================================================

import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict

input = sys.stdin.readline


# ============================================================
# [정렬 1] 백준 2751 수 정렬하기 2
#
# 문제:
# N개의 수가 주어졌을 때 오름차순 정렬해서 출력
#
# 여기서 이렇게 했다:
# 1. 수를 리스트에 저장
# 2. arr.sort()로 오름차순 정렬
# 3. print를 여러 번 하지 않고 join으로 한 번에 출력
# ============================================================

def solve_sort_numbers():
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    print("\n".join(map(str, arr)))


# ============================================================
# [정렬 2] 백준 11650 좌표 정렬하기
#
# 문제:
# 좌표 (x, y)를 x 오름차순으로 정렬
# x가 같으면 y 오름차순으로 정렬
#
# 여기서 이렇게 했다:
# 1. (x, y)를 튜플로 저장
# 2. Python 튜플 정렬은 기본적으로 첫 번째 값부터 비교함
# 3. 따라서 points.sort()만 해도 x → y 순서로 정렬됨
# ============================================================

def solve_coordinate_sort():
    n = int(input())

    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    points.sort()

    for x, y in points:
        print(x, y)


# ============================================================
# [정렬 3] 백준 10814 나이순 정렬
#
# 문제:
# 회원을 나이 오름차순으로 정렬
# 나이가 같으면 먼저 가입한 순서 유지
#
# 여기서 이렇게 했다:
# 1. 나이와 이름을 저장
# 2. key=lambda x: x[0]으로 나이만 기준으로 정렬
# 3. Python 정렬은 안정 정렬이라 나이가 같으면 기존 순서가 유지됨
# ============================================================

def solve_age_sort():
    n = int(input())

    members = []
    for _ in range(n):
        age, name = input().split()
        members.append((int(age), name))

    members.sort(key=lambda x: x[0])

    for age, name in members:
        print(age, name)


# ============================================================
# [정렬 4] 프로그래머스 베스트앨범
#
# 문제:
# 장르별로 가장 많이 재생된 노래를 최대 2개씩 뽑기
#
# 정렬 기준:
# 1. 장르 총 재생 수 내림차순
# 2. 장르 안에서는 노래 재생 수 내림차순
# 3. 재생 수가 같으면 고유번호 오름차순
#
# 여기서 이렇게 했다:
# 1. genre_total에 장르별 총 재생 수 저장
# 2. songs에 장르별 노래 목록 저장
# 3. 장르를 총 재생 수 기준으로 정렬
# 4. 각 장르 안에서 노래를 재생 수 내림차순, 번호 오름차순으로 정렬
# ============================================================

def solution_best_album(genres, plays):
    genre_total = defaultdict(int)
    songs = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        genre_total[genre] += play
        songs[genre].append((play, i))

    sorted_genres = sorted(genre_total.keys(), key=lambda g: -genre_total[g])

    answer = []

    for genre in sorted_genres:
        songs[genre].sort(key=lambda x: (-x[0], x[1]))

        for play, index in songs[genre][:2]:
            answer.append(index)

    return answer


# ============================================================
# [이진탐색 1] 백준 1920 수 찾기
#
# 문제:
# 주어진 숫자들이 배열 안에 존재하는지 확인
#
# 여기서 이렇게 했다:
# 1. 배열을 정렬
# 2. bisect_left로 target이 들어갈 가장 왼쪽 위치를 찾음
# 3. 그 위치의 값이 target이면 존재
# ============================================================

def solve_find_number():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    m = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        idx = bisect_left(arr, target)

        if idx < n and arr[idx] == target:
            print(1)
        else:
            print(0)


# ============================================================
# [이진탐색 2] 백준 10816 숫자 카드 2
#
# 문제:
# 각 숫자 카드가 몇 개 있는지 출력
#
# 여기서 이렇게 했다:
# 1. 카드를 정렬
# 2. target의 시작 위치 = bisect_left
# 3. target보다 큰 값의 시작 위치 = bisect_right
# 4. 개수 = right - left
# ============================================================

def solve_number_card_2():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()

    m = int(input())
    targets = list(map(int, input().split()))

    answer = []

    for target in targets:
        left = bisect_left(cards, target)
        right = bisect_right(cards, target)

        count = right - left
        answer.append(str(count))

    print(" ".join(answer))


# ============================================================
# [이진탐색 3] 백준 2805 나무 자르기
#
# 문제:
# 절단기 높이 H를 정해서 나무를 자른다.
# 적어도 M만큼의 나무를 가져가야 할 때 가능한 H의 최댓값 구하기
#
# 여기서 이렇게 했다:
# 1. 정답 후보는 0부터 가장 큰 나무 높이까지
# 2. mid 높이로 잘라본다
# 3. 가져갈 수 있는 나무 양이 M 이상이면 높이를 더 올려본다
# 4. 부족하면 높이를 낮춘다
# ============================================================

def solve_tree_cut():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    left = 0
    right = max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid

        if total >= m:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


# ============================================================
# [이진탐색 4] 백준 1654 랜선 자르기
#
# 문제:
# K개의 랜선을 잘라서 N개 이상의 랜선을 만들 때
# 가능한 랜선 길이의 최댓값 구하기
#
# 여기서 이렇게 했다:
# 1. 정답 후보는 1부터 가장 긴 랜선 길이까지
# 2. mid 길이로 잘랐을 때 몇 개가 나오는지 계산
# 3. N개 이상 만들 수 있으면 길이를 더 늘려본다
# 4. 부족하면 길이를 줄인다
# ============================================================

def solve_lan_cable():
    k, n = map(int, input().split())

    cables = []
    for _ in range(k):
        cables.append(int(input()))

    left = 1
    right = max(cables)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for cable in cables:
            count += cable // mid

        if count >= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


# ============================================================
# [이진탐색 5] 백준 2110 공유기 설치
#
# 문제:
# 집 N개 중 C개에 공유기를 설치한다.
# 가장 인접한 두 공유기 사이 거리의 최댓값을 구한다.
#
# 여기서 이렇게 했다:
# 1. 집 위치를 정렬
# 2. 정답 후보는 거리 1부터 최대 거리까지
# 3. mid 거리 이상 간격을 두고 공유기를 설치해본다
# 4. C개 이상 설치 가능하면 거리를 더 늘려본다
# 5. 부족하면 거리를 줄인다
# ============================================================

def solve_router_install():
    n, c = map(int, input().split())

    houses = []
    for _ in range(n):
        houses.append(int(input()))

    houses.sort()

    left = 1
    right = houses[-1] - houses[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        installed = 1
        last = houses[0]

        for i in range(1, n):
            if houses[i] - last >= mid:
                installed += 1
                last = houses[i]

        if installed >= c:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


# ============================================================
# [DP 1] 백준 1463 1로 만들기
#
# 문제:
# 정수 N을 1로 만들기 위한 최소 연산 횟수
#
# 가능한 연산:
# 1. 3으로 나누어 떨어지면 3으로 나누기
# 2. 2로 나누어 떨어지면 2로 나누기
# 3. 1 빼기
#
# 여기서 이렇게 했다:
# dp[i] = i를 1로 만드는 최소 연산 횟수
# 먼저 1을 빼는 경우를 넣고,
# 2 또는 3으로 나눌 수 있으면 더 작은 값으로 갱신
# ============================================================

def solve_make_one():
    n = int(input())

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[n])


# ============================================================
# [DP 2] 백준 9095 1, 2, 3 더하기
#
# 문제:
# 정수 n을 1, 2, 3의 합으로 나타내는 방법의 수 구하기
#
# 여기서 이렇게 했다:
# dp[i] = i를 만드는 경우의 수
# i를 만드는 마지막 숫자가 1이면 dp[i-1]
# 마지막 숫자가 2이면 dp[i-2]
# 마지막 숫자가 3이면 dp[i-3]
#
# 따라서:
# dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# ============================================================

def solve_123_sum():
    t = int(input())

    dp = [0] * 12
    dp[0] = 1

    for i in range(1, 12):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]

        if i - 2 >= 0:
            dp[i] += dp[i - 2]

        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    for _ in range(t):
        n = int(input())
        print(dp[n])


# ============================================================
# [DP 3] 백준 2579 계단 오르기
#
# 문제:
# 계단마다 점수가 있다.
# 마지막 계단은 반드시 밟아야 한다.
# 단, 연속된 세 계단은 밟을 수 없다.
#
# 여기서 이렇게 했다:
# dp[i] = i번째 계단까지 왔을 때 얻을 수 있는 최대 점수
#
# i번째 계단을 밟는 경우는 두 가지:
# 1. i-2에서 i로 바로 오는 경우
#    dp[i-2] + stairs[i]
#
# 2. i-3에서 i-1을 밟고 i로 오는 경우
#    dp[i-3] + stairs[i-1] + stairs[i]
# ============================================================

def solve_stair_score():
    n = int(input())

    stairs = []
    for _ in range(n):
        stairs.append(int(input()))

    if n == 1:
        print(stairs[0])
        return

    if n == 2:
        print(stairs[0] + stairs[1])
        return

    dp = [0] * n

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(
        stairs[0] + stairs[2],
        stairs[1] + stairs[2]
    )

    for i in range(3, n):
        dp[i] = max(
            dp[i - 2] + stairs[i],
            dp[i - 3] + stairs[i - 1] + stairs[i]
        )

    print(dp[n - 1])


# ============================================================
# [DP 4] 프로그래머스 정수 삼각형
#
# 문제:
# 삼각형 꼭대기에서 아래로 내려가며 선택한 숫자의 최대 합 구하기
#
# 여기서 이렇게 했다:
# dp[i][j] = i행 j열까지 내려왔을 때 가능한 최대 합
#
# 왼쪽 끝은 바로 위에서만 올 수 있음
# 오른쪽 끝은 왼쪽 위에서만 올 수 있음
# 가운데는 위쪽 두 칸 중 큰 값에서 옴
# ============================================================

def solution_integer_triangle(triangle):
    dp = [row[:] for row in triangle]

    for i in range(1, len(dp)):
        for j in range(len(dp[i])):

            if j == 0:
                dp[i][j] += dp[i - 1][j]

            elif j == len(dp[i]) - 1:
                dp[i][j] += dp[i - 1][j - 1]

            else:
                dp[i][j] += max(
                    dp[i - 1][j - 1],
                    dp[i - 1][j]
                )

    return max(dp[-1])


# ============================================================
# [DP 5] 프로그래머스 등굣길
#
# 문제:
# 집에서 학교까지 가는 최단 경로 개수 구하기
# 오른쪽과 아래쪽으로만 이동 가능
# 물웅덩이는 지나갈 수 없음
#
# 여기서 이렇게 했다:
# dp[y][x] = y, x 위치까지 오는 경로의 수
#
# 현재 칸으로 오는 방법:
# 1. 위에서 내려오기
# 2. 왼쪽에서 오른쪽으로 오기
#
# 따라서:
# dp[y][x] = dp[y-1][x] + dp[y][x-1]
# ============================================================

def solution_school_road(m, n, puddles):
    MOD = 1_000_000_007

    blocked = [[False] * (m + 1) for _ in range(n + 1)]

    for x, y in puddles:
        blocked[y][x] = True

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):

            if blocked[y][x]:
                dp[y][x] = 0
                continue

            if y == 1 and x == 1:
                continue

            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    return dp[n][m]


# ============================================================
# [DP 6] 프로그래머스 도둑질
#
# 문제:
# 원형으로 배치된 집에서 인접한 집을 털 수 없다.
# 훔칠 수 있는 돈의 최댓값 구하기
#
# 여기서 이렇게 했다:
# 원형이라 첫 집과 마지막 집은 동시에 털 수 없음
#
# 그래서 두 경우로 나눔:
# 1. 첫 집을 포함할 수 있는 경우 → 마지막 집 제외
# 2. 마지막 집을 포함할 수 있는 경우 → 첫 집 제외
#
# 일자형 도둑질은:
# dp[i] = i번째 집까지 봤을 때 훔칠 수 있는 최대 금액
# dp[i] = max(dp[i-1], dp[i-2] + money[i])
# ============================================================

def rob_linear(money):
    n = len(money)

    if n == 0:
        return 0

    if n == 1:
        return money[0]

    dp = [0] * n

    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, n):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + money[i]
        )

    return dp[-1]


def solution_steal(money):
    n = len(money)

    if n == 1:
        return money[0]

    case1 = rob_linear(money[:-1])
    case2 = rob_linear(money[1:])

    return max(case1, case2)


# ============================================================
# [DP 7] 백준 11053 가장 긴 증가하는 부분 수열
#
# 문제:
# 수열에서 증가하는 부분 수열 중 가장 긴 길이 구하기
#
# 여기서 이렇게 했다:
# dp[i] = i번째 숫자를 마지막으로 하는 증가 부분 수열의 최대 길이
#
# arr[j] < arr[i]라면
# j번째 뒤에 i번째 숫자를 붙일 수 있음
#
# 따라서:
# dp[i] = max(dp[i], dp[j] + 1)
# ============================================================

def solve_lis_dp():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


# ============================================================
# [DP + 이진탐색] LIS 빠른 버전
#
# 문제:
# 가장 긴 증가하는 부분 수열 길이를 O(N log N)에 구하기
#
# 여기서 이렇게 했다:
# lis 배열은 실제 정답 수열은 아니고,
# 각 길이별로 가능한 가장 작은 끝값을 저장한다.
#
# x가 들어갈 위치를 bisect_left로 찾고,
# 끝에 붙일 수 있으면 append,
# 아니면 해당 위치 값을 x로 교체한다.
# ============================================================

def solve_lis_binary():
    n = int(input())
    arr = list(map(int, input().split()))

    lis = []

    for x in arr:
        idx = bisect_left(lis, x)

        if idx == len(lis):
            lis.append(x)
        else:
            lis[idx] = x

    print(len(lis))


# ============================================================
# [실전 정렬 패턴 모음]
# ============================================================

def sort_pattern_examples():
    arr = [5, 1, 3, 2, 4]

    # 오름차순 정렬
    arr.sort()

    # 내림차순 정렬
    arr.sort(reverse=True)

    students = [
        ("kim", 90),
        ("lee", 80),
        ("park", 90)
    ]

    # 점수 오름차순
    students.sort(key=lambda x: x[1])

    # 점수 내림차순, 이름 오름차순
    students.sort(key=lambda x: (-x[1], x[0]))

    points = [(3, 4), (1, 2), (1, 1)]

    # x 오름차순, x 같으면 y 오름차순
    points.sort(key=lambda x: (x[0], x[1]))


# ============================================================
# [실전 이진탐색 패턴 모음]
# ============================================================

def binary_search_pattern_examples():
    arr = [1, 2, 2, 2, 3, 4, 5]

    # x가 존재하는지 확인
    x = 2
    idx = bisect_left(arr, x)

    if idx < len(arr) and arr[idx] == x:
        exists = True
    else:
        exists = False

    # x의 개수
    count_x = bisect_right(arr, x) - bisect_left(arr, x)

    # a 이상 b 이하 개수
    a = 2
    b = 4
    count_range = bisect_right(arr, b) - bisect_left(arr, a)

    return exists, count_x, count_range


# ============================================================
# [실전 DP 패턴 모음]
# ============================================================

def dp_pattern_examples():
    arr = [1, 2, 3, 1]

    # 인접한 것을 선택할 수 없는 경우
    # 예: 도둑질
    n = len(arr)
    dp = [0] * n

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + arr[i]
        )

    # 격자 경로 개수
    # dp[y][x] = 위에서 오는 경우 + 왼쪽에서 오는 경우
    rows = 3
    cols = 4

    grid_dp = [[0] * cols for _ in range(rows)]
    grid_dp[0][0] = 1

    for y in range(rows):
        for x in range(cols):
            if y == 0 and x == 0:
                continue

            up = grid_dp[y - 1][x] if y > 0 else 0
            left = grid_dp[y][x - 1] if x > 0 else 0

            grid_dp[y][x] = up + left

    return dp[-1], grid_dp[-1][-1]


# ============================================================
# 제출할 때 사용하는 부분
#
# 백준에 제출할 때는 아래에서 원하는 함수 하나만 호출하면 됨.
#
# 예시:
# solve_sort_numbers()
# solve_find_number()
# solve_tree_cut()
# solve_make_one()
# solve_lis_dp()
# ============================================================

if __name__ == "__main__":
    # 여기는 오픈북 정리용이라 기본 실행은 막아둠.
    # 백준 제출할 때 원하는 함수 하나만 주석 해제해서 사용.
    pass