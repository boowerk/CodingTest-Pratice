import sys

input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())

max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    prev_max = max_dp[:]
    prev_min = min_dp[:]

    max_dp[0] = max(prev_max[0], prev_max[1]) + a
    max_dp[1] = max(prev_max[0], prev_max[1], prev_max[2]) + b
    max_dp[2] = max(prev_max[1], prev_max[2]) + c

    min_dp[0] = min(prev_min[0], prev_min[1]) + a
    min_dp[1] = min(prev_min[0], prev_min[1], prev_min[2]) + b
    min_dp[2] = min(prev_min[1], prev_min[2]) + c

print(max(max_dp), min(min_dp))