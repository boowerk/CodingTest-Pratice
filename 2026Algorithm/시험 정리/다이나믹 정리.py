# ============================================================
# 실전용 Python 다이나믹 프로그래밍 DP 정리
# 핵심:
# 1. 큰 문제를 작은 문제로 나눌 수 있는가?
# 2. 같은 계산이 반복되는가?
# 3. dp[i]의 의미를 먼저 정해야 함
# ============================================================


# ============================================================
# 1. 피보나치 - Bottom Up
# dp[i] = i번째 피보나치 수
# ============================================================
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ============================================================
# 2. 1로 만들기 유형
# dp[i] = i를 1로 만드는 최소 연산 횟수
# 연산: -1, /2, /3
# ============================================================
def make_one(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]


# ============================================================
# 3. 계단 오르기
# dp[i] = i번째 계단까지 올라왔을 때 얻을 수 있는 최대 점수
# 조건: 연속된 세 계단을 밟을 수 없음
# ============================================================
def stair_score(scores):
    n = len(scores)

    if n == 0:
        return 0
    if n == 1:
        return scores[0]
    if n == 2:
        return scores[0] + scores[1]

    dp = [0] * n

    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, n):
        dp[i] = max(
            dp[i - 2] + scores[i],
            dp[i - 3] + scores[i - 1] + scores[i]
        )

    return dp[-1]


# ============================================================
# 4. 포도주 시식 유형
# dp[i] = i번째 잔까지 고려했을 때 마실 수 있는 최대 양
# 조건: 연속 3잔 마실 수 없음
# ============================================================
def wine_tasting(wines):
    n = len(wines)

    if n == 0:
        return 0
    if n == 1:
        return wines[0]
    if n == 2:
        return wines[0] + wines[1]

    dp = [0] * n

    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(
        dp[1],
        wines[0] + wines[2],
        wines[1] + wines[2]
    )

    for i in range(3, n):
        dp[i] = max(
            dp[i - 1],                         # 현재 잔 안 마심
            dp[i - 2] + wines[i],              # 현재 잔만 마심
            dp[i - 3] + wines[i - 1] + wines[i] # 이전 잔 + 현재 잔 마심
        )

    return dp[-1]


# ============================================================
# 5. 도둑질 / House Robber
# dp[i] = i번째 집까지 봤을 때 훔칠 수 있는 최대 금액
# 조건: 인접한 집을 털 수 없음
# ============================================================
def house_robber(money):
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
            dp[i - 1],          # 현재 집 안 털기
            dp[i - 2] + money[i] # 현재 집 털기
        )

    return dp[-1]


# ============================================================
# 6. 원형 도둑질
# 첫 집과 마지막 집이 인접한 경우
# 프로그래머스 도둑질 유형
# ============================================================
def circular_house_robber(money):
    n = len(money)

    if n == 1:
        return money[0]
    if n == 2:
        return max(money)

    # 첫 집을 터는 경우: 마지막 집 제외
    case1 = house_robber(money[:-1])

    # 첫 집을 안 터는 경우: 첫 집 제외
    case2 = house_robber(money[1:])

    return max(case1, case2)


# ============================================================
# 7. 정수 삼각형
# dp[i][j] = i행 j열까지 내려왔을 때 최대 합
# 프로그래머스 정수 삼각형 유형
# ============================================================
def integer_triangle(triangle):
    n = len(triangle)

    dp = [row[:] for row in triangle]

    for i in range(1, n):
        for j in range(len(triangle[i])):

            if j == 0:
                dp[i][j] += dp[i - 1][j]

            elif j == len(triangle[i]) - 1:
                dp[i][j] += dp[i - 1][j - 1]

            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[-1])


# ============================================================
# 8. 등굣길 / 격자 경로 개수
# dp[y][x] = 해당 위치까지 오는 경로의 수
# 오른쪽, 아래쪽으로만 이동 가능
# ============================================================
def school_road(m, n, puddles):
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
# 9. 가장 긴 증가하는 부분 수열 LIS - O(N^2)
# dp[i] = i번째 원소를 마지막으로 하는 LIS 길이
# ============================================================
def lis_dp(arr):
    n = len(arr)

    if n == 0:
        return 0

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# ============================================================
# 10. LIS - O(N log N)
# 실전에서는 이 버전도 자주 사용
# ============================================================
from bisect import bisect_left

def lis_binary_search(arr):
    lis = []

    for x in arr:
        idx = bisect_left(lis, x)

        if idx == len(lis):
            lis.append(x)
        else:
            lis[idx] = x

    return len(lis)


# ============================================================
# 11. 0/1 Knapsack
# dp[w] = 무게 w 이하에서 얻을 수 있는 최대 가치
# 각 물건은 한 번만 사용 가능
# ============================================================
def knapsack(items, max_weight):
    # items = [(weight, value), ...]

    dp = [0] * (max_weight + 1)

    for weight, value in items:
        for w in range(max_weight, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[max_weight]


# ============================================================
# 12. 동전 교환 - 최소 동전 개수
# dp[i] = i원을 만들기 위한 최소 동전 개수
# ============================================================
def coin_change_min(coins, target):
    INF = 10**9

    dp = [INF] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[target] == INF:
        return -1

    return dp[target]


# ============================================================
# 13. 동전 교환 - 경우의 수
# dp[i] = i원을 만드는 경우의 수
# 동전 순서만 다른 것은 같은 경우로 봄
# ============================================================
def coin_change_count(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]


# ============================================================
# 14. LCS
# 가장 긴 공통 부분 수열
# dp[i][j] = a[:i], b[:j]의 LCS 길이
# ============================================================
def lcs(a, b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


# ============================================================
# 15. 팰린드롬 DP
# dp[start][end] = start부터 end까지 팰린드롬인지 여부
# ============================================================
def palindrome_table(arr):
    n = len(arr)

    dp = [[False] * n for _ in range(n)]

    # 길이 1
    for i in range(n):
        dp[i][i] = True

    # 길이 2
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = True

    # 길이 3 이상
    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1

            if arr[start] == arr[end] and dp[start + 1][end - 1]:
                dp[start][end] = True

    return dp


# ============================================================
# 16. DP + DFS 메모이제이션
# 내리막길, 그래프 경로 개수 유형
# dp[y][x] = 해당 위치에서 목적지까지 가는 경로 수
# ============================================================
def downhill_path(board):
    import sys
    sys.setrecursionlimit(10**6)

    n = len(board)
    m = len(board[0])

    dp = [[-1] * m for _ in range(n)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def dfs(y, x):
        if y == n - 1 and x == m - 1:
            return 1

        if dp[y][x] != -1:
            return dp[y][x]

        dp[y][x] = 0

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] < board[y][x]:
                    dp[y][x] += dfs(ny, nx)

        return dp[y][x]

    return dfs(0, 0)


# ============================================================
# 실행 예시
# ============================================================
if __name__ == "__main__":
    print("피보나치:", fibonacci(10))
    print("1로 만들기:", make_one(10))

    print("계단 오르기:", stair_score([10, 20, 15, 25, 10, 20]))
    print("포도주 시식:", wine_tasting([6, 10, 13, 9, 8, 1]))

    print("도둑질:", house_robber([1, 2, 3, 1]))
    print("원형 도둑질:", circular_house_robber([1, 2, 3, 1]))

    triangle = [
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5]
    ]
    print("정수 삼각형:", integer_triangle(triangle))

    print("등굣길:", school_road(4, 3, [[2, 2]]))

    arr = [10, 20, 10, 30, 20, 50]
    print("LIS O(N^2):", lis_dp(arr))
    print("LIS O(N log N):", lis_binary_search(arr))

    items = [(6, 13), (4, 8), (3, 6), (5, 12)]
    print("Knapsack:", knapsack(items, 7))

    print("동전 최소 개수:", coin_change_min([1, 2, 5], 11))
    print("동전 경우의 수:", coin_change_count([1, 2, 5], 5))

    print("LCS:", lcs("ACAYKP", "CAPCAK"))

    board = [
        [9, 5, 3],
        [6, 4, 2],
        [7, 3, 1]
    ]
    print("내리막길 경로 수:", downhill_path(board))


# ============================================================
# 시험용 요약
# ============================================================
# 1. dp[i] 의미를 먼저 정한다.
#
# 2. 기본 1차원 DP
# dp[i] = min(dp[i - 1], dp[i - 2]) + cost
#
# 3. 최대/최소 선택
# dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
#
# 4. 2차원 경로 DP
# dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
#
# 5. 정수 삼각형
# dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
#
# 6. Knapsack
# for weight, value in items:
#     for w in range(max_weight, weight - 1, -1):
#         dp[w] = max(dp[w], dp[w - weight] + value)
#
# 7. 동전 경우의 수
# for coin in coins:
#     for amount in range(coin, target + 1):
#         dp[amount] += dp[amount - coin]
#
# 8. LIS O(N^2)
# if arr[j] < arr[i]:
#     dp[i] = max(dp[i], dp[j] + 1)
#
# 9. LCS
# if a[i - 1] == b[j - 1]:
#     dp[i][j] = dp[i - 1][j - 1] + 1
# else:
#     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# ============================================================