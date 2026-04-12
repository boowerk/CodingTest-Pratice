import sys
input = sys.stdin.readline

# 서로 바뀌어야 하는 흑백 개수를 세어 최소 작업 수를 구하는 풀이
T = int(input())

for _ in range(T):
    n = int(input())
    A = input().strip()
    B = input().strip()

    wb = 0
    bw = 0

    for i in range(n):
        # W->B와 B->W로 바뀌어야 하는 칸을 따로 센다.
        if A[i] == 'W' and B[i] == 'B':
            wb += 1
        elif A[i] == 'B' and B[i] == 'W':
            bw += 1

    # 서로 다른 색 교환과 개별 뒤집기를 섞으면 큰 쪽 개수만큼이면 충분하다.
    print(max(wb, bw))
