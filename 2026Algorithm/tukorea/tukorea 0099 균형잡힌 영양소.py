# 1개, 2개, 3개 음식 조합을 모두 보며 조건을 만족하는 경우를 센다.
n = int(input())
foods = [tuple(map(int, input().split())) for _ in range(n)]
limit_c, limit_p, limit_f, limit_k = map(int, input().split())

count = 0

def is_valid(c, p, f):
    # 탄수화물/단백질/지방 조건과 총 칼로리 제한을 동시에 검사한다.
    kcal = c * 4 + p * 4 + f * 9
    return c <= limit_c and p >= limit_p and f <= limit_f and kcal <= limit_k

# 음식 1개만 고르는 경우
for i in range(n):
    c, p, f = foods[i]
    if is_valid(c, p, f):
        count += 1

# 음식 2개를 고르는 모든 조합
for i in range(n):
    for j in range(i + 1, n):
        c = foods[i][0] + foods[j][0]
        p = foods[i][1] + foods[j][1]
        f = foods[i][2] + foods[j][2]
        if is_valid(c, p, f):
            count += 1

# 음식 3개를 고르는 모든 조합
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            c = foods[i][0] + foods[j][0] + foods[k][0]
            p = foods[i][1] + foods[j][1] + foods[k][1]
            f = foods[i][2] + foods[j][2] + foods[k][2]
            if is_valid(c, p, f):
                count += 1

print(count)
