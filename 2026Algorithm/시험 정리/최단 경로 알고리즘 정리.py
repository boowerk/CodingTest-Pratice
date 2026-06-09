from collections import deque
import heapq

# ============================================================
# 실전용 Python 최단 경로 알고리즘 정리
# 핵심:
# 1. 가중치가 없으면 BFS
# 2. 가중치가 0 또는 1이면 0-1 BFS
# 3. 가중치가 양수면 다익스트라
# 4. 음수 간선이 있으면 벨만-포드
# 5. 모든 정점 간 최단 거리는 플로이드-워셜
# ============================================================


# ============================================================
# 1. 무가중치 최단 거리 - BFS
# 간선 비용이 모두 1일 때 사용한다.
# ============================================================
def bfs_shortest_path(graph, start, n):
    dist = [-1] * (n + 1)
    queue = deque([start])
    dist[start] = 0

    while queue:
        now = queue.popleft()

        # BFS에서는 먼저 방문한 거리가 항상 최단 거리다.
        for next_v in graph[now]:
            if dist[next_v] == -1:
                dist[next_v] = dist[now] + 1
                queue.append(next_v)

    return dist


# ============================================================
# 2. 0-1 BFS
# 간선 비용이 0 또는 1만 있을 때 다익스트라보다 빠르게 풀 수 있다.
# ============================================================
def zero_one_bfs(graph, start, n):
    INF = 10**18
    dist = [INF] * (n + 1)
    queue = deque([start])
    dist[start] = 0

    while queue:
        now = queue.popleft()

        for next_v, cost in graph[now]:
            new_cost = dist[now] + cost

            if new_cost >= dist[next_v]:
                continue

            dist[next_v] = new_cost

            # 비용 0은 앞에 넣고 비용 1은 뒤에 넣어 작은 거리부터 처리한다.
            if cost == 0:
                queue.appendleft(next_v)
            else:
                queue.append(next_v)

    return dist


# ============================================================
# 3. 다익스트라 기본
# 음수 간선이 없는 그래프에서 시작점 기준 최단 거리를 구한다.
# ============================================================
def dijkstra(graph, start, n):
    INF = 10**18
    dist = [INF] * (n + 1)
    heap = []

    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        current_cost, now = heapq.heappop(heap)

        # 이미 더 짧은 경로가 확정된 상태면 버린다.
        if current_cost > dist[now]:
            continue

        for next_v, cost in graph[now]:
            new_cost = current_cost + cost

            if new_cost < dist[next_v]:
                dist[next_v] = new_cost
                heapq.heappush(heap, (new_cost, next_v))

    return dist


# ============================================================
# 4. 다익스트라 + 경로 복원
# 최소 비용뿐 아니라 실제 지나간 노드 순서가 필요할 때 사용한다.
# ============================================================
def dijkstra_restore_path(graph, start, target, n):
    INF = 10**18
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    heap = [(0, start)]
    dist[start] = 0

    while heap:
        current_cost, now = heapq.heappop(heap)

        if current_cost > dist[now]:
            continue

        for next_v, cost in graph[now]:
            new_cost = current_cost + cost

            if new_cost < dist[next_v]:
                dist[next_v] = new_cost
                parent[next_v] = now
                heapq.heappush(heap, (new_cost, next_v))

    if dist[target] == INF:
        return INF, []

    # target에서 parent를 거꾸로 따라가면 최단 경로가 복원된다.
    path = []
    current = target
    while current != -1:
        path.append(current)
        current = parent[current]

    return dist[target], path[::-1]


# ============================================================
# 5. 특정 정점을 반드시 거치는 최단 경로
# 예: 1 -> v1 -> v2 -> n 또는 1 -> v2 -> v1 -> n 중 작은 값
# ============================================================
def shortest_path_via_two_nodes(graph, n, v1, v2):
    INF = 10**18

    dist_from_1 = dijkstra(graph, 1, n)
    dist_from_v1 = dijkstra(graph, v1, n)
    dist_from_v2 = dijkstra(graph, v2, n)

    # 두 가지 방문 순서 중 가능한 최솟값을 고른다.
    case1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
    case2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]
    answer = min(case1, case2)

    if answer >= INF:
        return -1
    return answer


# ============================================================
# 6. 2차원 격자 다익스트라
# 칸마다 이동 비용이 다를 때 사용한다.
# ============================================================
def grid_dijkstra(board):
    INF = 10**18
    n = len(board)
    m = len(board[0])
    dist = [[INF] * m for _ in range(n)]
    heap = [(board[0][0], 0, 0)]
    dist[0][0] = board[0][0]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while heap:
        current_cost, x, y = heapq.heappop(heap)

        if current_cost > dist[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            new_cost = current_cost + board[nx][ny]

            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))

    return dist[n - 1][m - 1]


# ============================================================
# 7. 플로이드-워셜
# 모든 노드에서 모든 노드까지 최단 거리를 구한다.
# n이 작을 때 사용한다. 보통 O(N^3)
# ============================================================
def floyd_warshall(n, edges):
    INF = 10**18
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for a, b, cost in edges:
        # 같은 간선이 여러 번 들어오면 더 작은 비용만 남긴다.
        dist[a][b] = min(dist[a][b], cost)

    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if dist[start][end] > dist[start][mid] + dist[mid][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]

    return dist


# ============================================================
# 8. 벨만-포드
# 음수 간선이 있을 수 있을 때 사용한다.
# n번째에도 갱신되면 음수 사이클이 존재한다.
# ============================================================
def bellman_ford(n, edges, start):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[start] = 0

    for i in range(n):
        updated = False

        for a, b, cost in edges:
            if dist[a] == INF:
                continue

            if dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                updated = True

                # n번째 반복에서 갱신되면 음수 사이클이다.
                if i == n - 1:
                    return True, dist

        if not updated:
            break

    return False, dist


# ============================================================
# 9. K번째 최단 경로
# 각 노드마다 최단 거리 후보를 최대 K개까지 저장한다.
# ============================================================
def kth_shortest_path(graph, start, n, k):
    distances = [[] for _ in range(n + 1)]
    heap = [(0, start)]
    heapq.heappush(distances[start], 0)

    while heap:
        current_cost, now = heapq.heappop(heap)

        for next_v, cost in graph[now]:
            new_cost = current_cost + cost

            if len(distances[next_v]) < k:
                heapq.heappush(distances[next_v], -new_cost)
                heapq.heappush(heap, (new_cost, next_v))

            elif -distances[next_v][0] > new_cost:
                # 가장 큰 후보를 빼고 더 작은 새 후보를 넣는다.
                heapq.heappop(distances[next_v])
                heapq.heappush(distances[next_v], -new_cost)
                heapq.heappush(heap, (new_cost, next_v))

    answer = [-1] * (n + 1)
    for i in range(1, n + 1):
        if len(distances[i]) == k:
            answer[i] = -distances[i][0]

    return answer


# ============================================================
# 시험용 선택 기준
# ============================================================
# 1. "간선 수", "이동 횟수", "최소 칸 수"처럼 비용이 모두 같으면 BFS
#
# 2. "순간이동 0초, 걷기 1초"처럼 비용이 0/1이면 0-1 BFS
#
# 3. "도로 비용", "택배 비용", "위험도"가 모두 양수면 다익스트라
#
# 4. "시간을 되돌리는 도로", "수익/손해"처럼 음수가 있으면 벨만-포드
#
# 5. "모든 도시 쌍", "A에서 B까지 갈 수 있는가"가 많고 n이 작으면 플로이드-워셜
#
# 6. 다익스트라에서 heap에 같은 노드가 여러 번 들어갈 수 있으므로
#    if current_cost > dist[now]: continue 처리가 중요하다.
#
# 7. 도달 불가능 처리는 INF 그대로인지 확인하고 보통 -1 또는 "INF"로 출력한다.
# ============================================================


if __name__ == "__main__":
    # 다익스트라 사용 예시
    n = 5
    graph = [[] for _ in range(n + 1)]
    sample_edges = [
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 1),
        (2, 4, 2),
        (3, 5, 3),
        (4, 5, 1),
    ]

    for a, b, cost in sample_edges:
        graph[a].append((b, cost))

    print(dijkstra(graph, 1, n))
    print(dijkstra_restore_path(graph, 1, 5, n))
