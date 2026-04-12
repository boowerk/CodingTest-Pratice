from collections import deque

# 현재 위치에서 -1, +1, *2 이동을 BFS로 탐색하는 최단 거리 풀이
n, k = map(int, input().split())

MAX = 100001
# visited[x]에는 x 위치까지 가는 최소 시간을 저장한다.
visited = [-1] * MAX

def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]

        # 한 번의 이동으로 갈 수 있는 세 가지 경우를 모두 확인한다.
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs(n))
