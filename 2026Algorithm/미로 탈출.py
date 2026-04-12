from collections import deque

# BFS로 시작점부터 각 칸의 최단 거리를 채워 나가는 풀이

def bfs(x, y):
    queue = deque()
    # 시작 칸을 큐에 넣고 탐색을 시작한다.
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어날 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 기록
            if graph[nx][ny] == 1:
                # 현재 칸 거리 + 1로 다음 칸의 최단 거리를 저장한다.
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지 최단 거리 반환
    return graph[n - 1][m -1]

# 미로의 세로, 가로 크기를 입력받는다.
n, m = map(int, input().split())

graph = []

for i in range(n):
    # 문자열 형태의 한 줄을 숫자 리스트로 바꿔 저장한다.
    graph.append(list(map(int, input())))

# 상하좌우 이동용 방향 배열이다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
