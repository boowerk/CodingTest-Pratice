from collections import deque

# DFS를 상황별로 바로 재사용할 수 있게 정리한 예제 파일

# 그래프 DFS - 재귀
# 연결 요소 개수, 방문 가능한 노드 탐색, 경로 존재 여부, 네트워크 / 타겟 탐색류
def dfs(graph, v, visited):
    visited[v] = True

    # 현재 노드에서 갈 수 있는 다음 노드를 끝까지 내려가며 방문한다.
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(graph, next_v, visited)

# 사용 예시
n = 5   # 노드 개수
graph = [[] for _ in range(n)]

# graph = [
#     [],         # 0번은 안 쓰는 경우
#     [2, 3],     # 1번 노드와 연결된 노드들
#     [1, 4],
#     [1, 5],
#     [2],
#     [3]
# ]

visited = [False] * (n + 1)

dfs(graph, 1, visited)
print(visited)

# ---------------------------------------------------------

# 그래프 DFS - 스택
# 재귀 깊이 걱정될 때 사용
# 큰 입력에서도 안전하게 돌리기 좋음
def dfs_stack(graph, start, n):
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True

    while(stack):
        # 스택은 가장 마지막에 넣은 노드부터 꺼내며 깊게 탐색한다.
        now = stack.pop()

        for next_v in graph[now]:
            if not visited[next_v]:
                visited[next_v] = True
                stack.append(next_v)

    return visited

# 사용예시
n = 5
graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2],
    [3]
]

result = dfs_stack(graph, 1, n)
print(result)

# ---------------------------------------------------------

# 2차원 배열 DFS
# 섬 개수, 그림 개수, 영역 개수, 상하좌우 연결 탐색
def dfs(x, y, maps, visited, n, m):
    visited[x][y] = True

    # 상 하 좌 우
    dx = [-1, -1, 0, 0]
    dy = [0, 0, -1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 방문 안했고, 탐색 가능한 칸이면 진행
        if not visited[nx][ny]  and maps[nx][ny] == 1:
            dfs(nx, ny, maps, visited, n, m)

# 사용 예시
maps = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

n = len(maps)
m = len(maps[0])
visited = [[False] * m for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and not visited[i][j]:
            dfs(i, j, maps, visited, n, m)
            count += 1

print(count)

# ---------------------------------------------------------

# 연결 요소 개수 세기 템플릿
# 네트워크, 그룹 개수, 컴포넌트 개수
def dfs(graph, v, visited):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(graph, next_v, visited)

def count_components(n, graph):
    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            # 아직 방문하지 않은 노드에서 DFS를 시작하면 새로운 컴포넌트다.
            dfs(graph, i, visited)
            count += 1

    return count

# ---------------------------------------------------------

# 네트워크형 템플릿
# computers 같이 인접행렬로 들어오는 문제
def dfs(computers, visited, now):
    visited[now] = True
    n = len(computers)

    for next_v in range(n):
        # 자기 자신 제외, 연결되어 있고, 아직 방문 안했으면 진행
        if now != next_v and computers[now][next_v] == 1 and not visited[next_v]:
            dfs(computers, visited, next_v)

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            # 연결된 컴퓨터 묶음을 하나 찾을 때마다 네트워크 개수를 늘린다.
            dfs(computers, visited, i)
            answer += 1

        return answer

# ---------------------------------------------------------

# 백트래킹형 DFS 템플릿
# 조합, 순열, 완전탐색도 섞여 나올 수 있음
def dfs(depth, path, used, arr):
    # 원하는 길이에 도달하면 결과 처리
    if depth == len(arr):
        print(path[:])
        return

    for i in range(len(arr)):
        if not used[i]:
            # 현재 원소를 선택하고 다음 깊이로 내려간 뒤, 복구하며 다른 경우를 본다.
            used[i] = True
            path.append(arr[i])

            dfs(depth + 1, path, used, arr)

            path.pop()
            used[i] = False

# 사용 예시
arr = [1, 2, 3]
used = [False] * len(arr)
dfs(0, [], used, arr)









































