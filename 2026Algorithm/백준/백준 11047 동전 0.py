# 큰 동전부터 greedily 사용해 최소 동전 수를 구하는 풀이
N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

count = 0

for i in range(N - 1, -1, -1):
    # 현재 동전을 최대한 많이 사용한 뒤 남은 금액만 다음 동전으로 넘긴다.
    count += K // coins[i]
    K %= coins[i]

print(count)
