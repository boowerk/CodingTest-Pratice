import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    A = input().strip()
    B = input().strip()

    wb = 0
    bw = 0

    for i in range(n):
        if A[i] == 'W' and B[i] == 'B':
            wb += 1
        elif A[i] == 'B' and B[i] == 'W':
            bw += 1

    print(max(wb, bw))