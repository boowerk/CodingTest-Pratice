import sys
input = sys.stdin.readline

N = int(input())

Cows = []

for _ in range(N):
    s, e = map(int, input().split())
    Cows.append((s, e))

Cows.sort()

time = 0

for s, e in Cows:
    time = max(time, s) + e

print(time)
