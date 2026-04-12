# 카드 3장을 모두 조합해 제한 이하의 최댓값을 찾는 완전탐색 풀이
n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            # 세 장의 합이 m을 넘지 않을 때만 정답 후보로 사용한다.
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                answer = max(answer, total)

print(answer)
