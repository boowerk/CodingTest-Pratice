# ============================================================
# 실전용 Python 정렬 정리
# 코딩테스트에서는 대부분 직접 정렬 구현 X
# arr.sort(), sorted(), key=lambda 사용이 핵심
# ============================================================


# ------------------------------------------------------------
# 1. 기본 정렬
# ------------------------------------------------------------
arr = [5, 2, 9, 1, 7]

arr.sort()                  # 원본 리스트 자체를 오름차순 정렬
print(arr)                  # [1, 2, 5, 7, 9]

arr = [5, 2, 9, 1, 7]
new_arr = sorted(arr)       # 정렬된 새 리스트 반환, 원본 유지
print(new_arr)              # [1, 2, 5, 7, 9]


# ------------------------------------------------------------
# 2. 내림차순 정렬
# ------------------------------------------------------------
arr = [5, 2, 9, 1, 7]

arr.sort(reverse=True)
print(arr)                  # [9, 7, 5, 2, 1]

new_arr = sorted(arr, reverse=True)
print(new_arr)


# ------------------------------------------------------------
# 3. 튜플 / 리스트 정렬
# ------------------------------------------------------------
data = [
    ("kim", 90),
    ("lee", 80),
    ("park", 95),
    ("choi", 80)
]

# 점수 기준 오름차순
data.sort(key=lambda x: x[1])
print(data)

# 점수 기준 내림차순
data.sort(key=lambda x: x[1], reverse=True)
print(data)

# 이름 기준 오름차순
data.sort(key=lambda x: x[0])
print(data)


# ------------------------------------------------------------
# 4. 여러 기준 정렬
# ------------------------------------------------------------
students = [
    ("kim", 90),
    ("lee", 80),
    ("park", 95),
    ("choi", 80),
    ("ahn", 90)
]

# 점수 오름차순, 점수가 같으면 이름 오름차순
students.sort(key=lambda x: (x[1], x[0]))
print(students)

# 점수 내림차순, 점수가 같으면 이름 오름차순
students.sort(key=lambda x: (-x[1], x[0]))
print(students)

# 점수 오름차순, 점수가 같으면 이름 내림차순
# 문자열 내림차순은 reverse=True와 섞이면 헷갈리므로 필요하면 아래 방식 사용
students.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(students)


# ------------------------------------------------------------
# 5. 2차원 배열 정렬
# ------------------------------------------------------------
points = [
    [3, 4],
    [1, 2],
    [1, 1],
    [2, 5],
    [3, 1]
]

# x 오름차순, x가 같으면 y 오름차순
points.sort(key=lambda x: (x[0], x[1]))
print(points)

# y 오름차순, y가 같으면 x 오름차순
points.sort(key=lambda x: (x[1], x[0]))
print(points)

# x 오름차순, y 내림차순
points.sort(key=lambda x: (x[0], -x[1]))
print(points)


# ------------------------------------------------------------
# 6. 문자열 정렬
# ------------------------------------------------------------
words = ["apple", "banana", "kiwi", "cat", "grape"]

# 사전순 정렬
words.sort()
print(words)

# 길이순 정렬
words.sort(key=len)
print(words)

# 길이순, 길이가 같으면 사전순
words.sort(key=lambda x: (len(x), x))
print(words)


# ------------------------------------------------------------
# 7. 자주 나오는 패턴: 국영수 정렬
# 조건:
# 국어 점수 내림차순
# 영어 점수 오름차순
# 수학 점수 내림차순
# 이름 사전순 오름차순
# ------------------------------------------------------------
students = [
    ["Junkyu", 50, 60, 100],
    ["Sangkeun", 80, 60, 50],
    ["Sunyoung", 80, 70, 100],
    ["Soong", 50, 60, 90],
    ["Haebin", 50, 60, 100]
]

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])


# ------------------------------------------------------------
# 8. 객체 / 딕셔너리 정렬
# ------------------------------------------------------------
players = [
    {"name": "kim", "score": 90},
    {"name": "lee", "score": 80},
    {"name": "park", "score": 95}
]

# score 기준 오름차순
players.sort(key=lambda x: x["score"])
print(players)

# score 기준 내림차순
players.sort(key=lambda x: -x["score"])
print(players)


# ------------------------------------------------------------
# 9. 빈도수 정렬
# ------------------------------------------------------------
from collections import Counter

arr = [1, 3, 2, 3, 2, 3, 1, 4, 2]

counter = Counter(arr)

# 많이 나온 순서대로 정렬
result = sorted(counter.items(), key=lambda x: -x[1])
print(result)               # [(3, 3), (2, 3), (1, 2), (4, 1)]

# 빈도 내림차순, 값 오름차순
result = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
print(result)


# ------------------------------------------------------------
# 10. 중복 제거 후 정렬
# ------------------------------------------------------------
arr = [5, 1, 3, 5, 2, 1, 4]

result = sorted(set(arr))
print(result)               # [1, 2, 3, 4, 5]


# ------------------------------------------------------------
# 11. 좌표 압축
# 자주 나오는 실전 패턴
# ------------------------------------------------------------
arr = [1000, 999, 1000, 999, 1001]

sorted_unique = sorted(set(arr))

rank = {}
for i, value in enumerate(sorted_unique):
    rank[value] = i

result = []
for x in arr:
    result.append(rank[x])

print(result)               # [1, 0, 1, 0, 2]


# 더 짧은 버전
arr = [1000, 999, 1000, 999, 1001]
rank = {value: i for i, value in enumerate(sorted(set(arr)))}
result = [rank[x] for x in arr]
print(result)


# ------------------------------------------------------------
# 12. 가장 큰 값 / 작은 값 K개
# 전체 정렬 사용
# ------------------------------------------------------------
arr = [5, 1, 9, 3, 7, 2, 8]
k = 3

smallest = sorted(arr)[:k]
largest = sorted(arr, reverse=True)[:k]

print(smallest)             # [1, 2, 3]
print(largest)              # [9, 8, 7]


# ------------------------------------------------------------
# 13. heapq로 K개 뽑기
# 데이터가 많을 때 유용
# ------------------------------------------------------------
import heapq

arr = [5, 1, 9, 3, 7, 2, 8]
k = 3

smallest = heapq.nsmallest(k, arr)
largest = heapq.nlargest(k, arr)

print(smallest)
print(largest)


# ------------------------------------------------------------
# 14. 정렬된 상태에서 이분 탐색
# ------------------------------------------------------------
from bisect import bisect_left, bisect_right

arr = [1, 2, 2, 2, 3, 4, 5]

# 값 2가 처음 등장하는 위치
left = bisect_left(arr, 2)

# 값 2보다 큰 값이 처음 등장하는 위치
right = bisect_right(arr, 2)

print(left)                 # 1
print(right)                # 4

# 값 2의 개수
count = right - left
print(count)                # 3


# ------------------------------------------------------------
# 15. 정렬 후 그리디 예시
# 회의실 배정 유형
# 끝나는 시간 기준 정렬, 같으면 시작 시간 기준 정렬
# ------------------------------------------------------------
meetings = [
    [1, 4],
    [3, 5],
    [0, 6],
    [5, 7],
    [3, 8],
    [5, 9],
    [6, 10],
    [8, 11],
    [8, 12],
    [2, 13],
    [12, 14]
]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)


# ------------------------------------------------------------
# 16. 정렬 후 투 포인터 예시
# 두 수의 합 찾기
# ------------------------------------------------------------
arr = [1, 4, 2, 3, 7, 5]
target = 9

arr.sort()

left = 0
right = len(arr) - 1
found = False

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        found = True
        break
    elif total < target:
        left += 1
    else:
        right -= 1

print(found)


# ------------------------------------------------------------
# 17. 실전 입력 예시
# ------------------------------------------------------------
# 입력:
# 5
# kim 90
# lee 80
# park 95
# choi 80
# ahn 90

"""
n = int(input())
data = []

for _ in range(n):
    name, score = input().split()
    data.append((name, int(score)))

# 점수 내림차순, 이름 오름차순
data.sort(key=lambda x: (-x[1], x[0]))

for name, score in data:
    print(name, score)
"""


# ============================================================
# 실전 요약
# ============================================================
# 1. 원본 정렬
# arr.sort()
#
# 2. 새 리스트 반환
# sorted(arr)
#
# 3. 내림차순
# arr.sort(reverse=True)
#
# 4. 기준 정렬
# arr.sort(key=lambda x: x[1])
#
# 5. 여러 기준 정렬
# arr.sort(key=lambda x: (x[0], x[1]))
#
# 6. 내림차순 기준 섞기
# arr.sort(key=lambda x: (-x[1], x[0]))
#
# 7. 중복 제거 후 정렬
# sorted(set(arr))
#
# 8. 빈도수 정렬
# sorted(counter.items(), key=lambda x: (-x[1], x[0]))
#
# 9. 좌표 압축
# rank = {v: i for i, v in enumerate(sorted(set(arr)))}
#
# 10. 정렬 + 이분 탐색
# bisect_left(arr, x), bisect_right(arr, x)
# ============================================================