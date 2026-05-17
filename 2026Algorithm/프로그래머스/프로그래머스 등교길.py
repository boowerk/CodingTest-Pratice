def solution(m, n, puddles):
    MOD = 1000000007

    # dp[y][x] 형태로 사용
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 물웅덩이 위치 저장
    puddle_set = set()
    for x, y in puddles:
        puddle_set.add((x, y))

    # 시작 위치
    dp[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            # 시작점은 이미 처리했으므로 건너뜀
            if x == 1 and y == 1:
                continue

            # 물웅덩이면 갈 수 없음
            if (x, y) in puddle_set:
                dp[y][x] = 0
            else:
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    return dp[n][m]