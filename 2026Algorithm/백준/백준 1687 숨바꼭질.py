from collections import deque

n, k = map(int, input().split())

MAX = 100001
visited = [-1] * MAX

def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs(n))
