n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]

houses.sort()

left = 1
right = houses[-1] - houses[0]

answer = 0

while left <= right:
    mid = (left + right) // 2

    count = 1

    last = houses[0]

    for i in range(1, n):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    if count >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)