import sys
input = sys.stdin.readline

T = int(input())

meetings = []

for _ in range(T):
    s, e = map(int, input().split())

    meetings.append((s, e))

meetings.sort(key= lambda x: (x[1], x[0]))

count = 0
last_end = 0

for s, e in meetings:
    if s >= last_end:
        count += 1
        last_end = e

print(count)
