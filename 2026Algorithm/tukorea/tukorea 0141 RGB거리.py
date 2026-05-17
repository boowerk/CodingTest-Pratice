import sys

input = sys.stdin.readline

n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

dp[0][0] = cost[0][0]  # 첫 번째 집을 빨강
dp[0][1] = cost[0][1]  # 첫 번째 집을 초록
dp[0][2] = cost[0][2]  # 첫 번째 집을 파랑

for i in range(1, n):
    # i번째 집을 빨강으로 칠하는 경우
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]

    # i번째 집을 초록으로 칠하는 경우
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]

    # i번째 집을 파랑으로 칠하는 경우
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

print(min(dp[n - 1]))