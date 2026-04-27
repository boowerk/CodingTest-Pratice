n = int(input())
requests = list(map(int, input().split()))
m = int(input())

left = 0
right = max(requests)
answer = 0

while left <= right:
    mid = (left + right) // 2

    total = 0
    for r in requests:
        total += min(r, mid)

    if total <= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)