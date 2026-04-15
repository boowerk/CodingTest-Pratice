import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input(T))

    answer = 0

    for _ in range(N):
        a, b, c = map(int, input().split())
        answer += max(0, a, b, c)

    print(answer)