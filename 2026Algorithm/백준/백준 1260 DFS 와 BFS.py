from collections import deque
import sys

# 같은 그래프를 DFS와 BFS로 각각 순회하는 기본 풀이
input = sys.stdin.readline # 입력 속도 개선

# n: 정점 개수, m: 간선 개수, v: 시작 정점
n, m, v = map(int, input().split())

# 그래프를 인접 리스트로 표현 (1번부터 n번까지 사용)
graph = [[] for _ in range(n + 1)]

# 간선 입력 (양방향 그래프이므로 양쪽에 모두 추가)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# "작은 번호부터 방문" 조건 때문에 정렬 필수
for i in range(1, n + 1):
    graph[i].sort()

# ---------------- DFS ----------------
def dfs(x, visited):
    visited[x] = True   # 현재 노드 방문 처리
    print(x, end=' ')   # 방문 순서 출력

    # 현재 노드와 연결된 다른 노드 확인
    for nxt in graph[x]:
        if not visited[nxt]:    # 아직 방문하지 않았다면
            dfs(nxt, visited)   # 재귀적으로 방문

# ---------------- BFS ----------------
def bfs(start):
    visited = [False] * (n + 1) # BFS용 방문 배열 (DFS와 따로)
    q = deque([start])          # 큐 생성 + 시작 노드 삽입
    visited[start] = True       # 시작 노드 방문 처리

    while q:
        x = q.popleft()         # 큐에서 하나 꺼냄
        print(x, end=' ')       # 방문 순서 출력

        # 현재 노드와 연결된 노드를 확인
        for nxt in graph[x]:
            if not visited[nxt]:    # 아직 방문하지 않았다면
                visited[nxt] = True     # 방문 처리
                q.append(nxt)           # 큐에 삽입

visited_dfs  = [False] * (n + 1)
dfs(v, visited_dfs)

print()

bfs(v)
