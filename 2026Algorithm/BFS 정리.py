from collections import deque

# BFS를 문제 유형별로 빠르게 꺼내 쓰기 위한 템플릿 모음

# 그래프 BFS - 기본
# 최단 거리, 레벨 탐색, 가장 먼저 도착하는 문제, 네트워크 / 변환 / 이동 횟수 문제
def bfs(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()

        # 현재 노드와 연결된 노드를 차례대로 확장한다.
        for next_v in graph[now]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

        # 방문 가능 여부만 확인하는 기본형 예시라 visited를 바로 반환한다.
        return visited

# 사용 예시
n = 5
graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2],
    [3]
]

result = bfs(graph, 1, n)
print(result)

# ---------------------------------------------------------

# 그래프 BFS - 최단 거리
# 시작점에서 각 노드까지 최소 이동 거리
def bfs_distance(graph, start, n):
    dist = [-1] * (n + 1)   # -1이면 아직 방문 안 함
    queue = deque([start])
    dist[start] = 0

    while queue:
        now = queue.popleft()

        for next_v in graph[now]:
            if dist[next_v] == -1:
                dist[next_v] = dist[now] + 1
                queue.append(next_v)

    return dist

# 사용 예시
n = 6
graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2, 6],
    [3],
    [4]
]

dist = bfs_distance(graph, 1, n)
print(dist)  # 1번 노드에서 각 노드까지 거리

# ---------------------------------------------------------

# 2차원 배열 BFS
# 미로 탐색, 게임 맵 최단거리, 상하좌우 이동 문제

def bfs(start_x, start_y, maps):
    n = len(maps)
    m = len(maps[0])

    # 거리 배열: -1이면 미방문
    dist = [[-1] * m for _ in range(n)]
    queue = deque([(start_x, start_y)])
    dist[start_x][start_y] = 1      # 시작 칸 포함이면 1, 아니면 0으로 시작해도 됨

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        # 현재 칸에서 4방향으로 한 칸씩 움직이며 탐색한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이면 못 감
            if maps[nx][ny] == 0:
                continue

            # 처음 방문하는 칸이면 거리 갱신
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist

# 사용 예시
maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

dist = bfs(0, 0, maps)
print(dist)

# 도착점 거리
n = len(maps)
m = len(maps[0])
print(dist[n - 1][m - 1])

# ---------------------------------------------------------

# 8방향 탐색 템플릿
# 대각선 포함, 섬 문제, 그림 문제, 지뢰찾기류
def bfs_8dir(start_x, start_y, maps, visited):
    n = len(maps)
    m = len(maps[0])

    # 상하좌우 + 대각선 4개
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y, = queue.popleft()

        # 대각선을 포함한 8방향 칸을 모두 확인한다.
        for i in range(8):
            nx = x + dy[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

# ---------------------------------------------------------

# 단어 변환 / 레벨 이동형 BFS 템플릿
# 한 번에 한 글자만 바뀌는 문제, 상태 변환형 BFS
def can_change(a, b):
    # 두 문자열이 한 글자만 다른지 확인
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)]) # (현재 단어, 변환 횟수)
    visited = [False] * len(words)

    while queue:
        now, count = queue.popleft()

        # 목표 단어를 찾는 순간 현재까지의 변환 횟수를 반환한다.
        if now == target:
            return count

        for i in range(len(words)):
            if not visited[i] and can_change(now, words[i]):
                visited[i] = True
                queue.append((words[i], count + 1))

    return 0

# ---------------------------------------------------------

# 상태 저장 BFS 템플릿
# 방문 배열이 1개로 안되는 문제
# 벽 부수기, 레버 상태, 아이템 획득 여부, 상태까지 같이 방문 처리해야 함.

def bfs():
    # 예시: (x, y, state)
    queue = deque()
    queue.append((0, 0, 0))     # state는 문제 조건에 맞게 의미 부여

    n, m = 5, 5

    # visited[x][y][state]
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, state = queue.popleft()

        # 좌표뿐 아니라 상태까지 함께 관리해야 같은 칸도 다시 방문할 수 있다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            new_state = state

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 조건에 따라 state 변경
            # 예: 레버를 만나면 new_state = 1

            if not visited[nx][ny][new_state]:
                visited[nx][ny][new_state] = True
                queue.append((nx, ny, new_state))

# ---------------------------------------------------------
# 게임 맵 최단거리

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque([(0, 0)])
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        # BFS이므로 먼저 도착한 경로가 곧 최단 거리다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maps[nx][ny] == 0:
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist[n - 1][m - 1]




































