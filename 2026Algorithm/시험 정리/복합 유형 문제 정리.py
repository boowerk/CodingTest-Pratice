from collections import Counter, defaultdict, deque
import heapq
import math

# ============================================================
# 실전용 Python 복합 유형 문제 정리
# 핵심:
# 1. 문제 이름은 BFS인데 visited에 상태가 추가될 수 있다.
# 2. "최소의 최대값", "가능한가?"는 이분 탐색 + 판정 함수로 바꿔 본다.
# 3. 방향 그래프의 순서 문제는 위상 정렬 + DP가 자주 붙는다.
# 4. 최단 경로에 쿠폰, 포장, 벽 부수기 같은 조건이 붙으면 상태를 나눈다.
# 5. 구간 문제는 누적합, 해시, 투 포인터가 섞여 나올 수 있다.
# ============================================================


# ============================================================
# 1. BFS + 상태 관리
# 벽을 한 번까지 부수고 이동할 수 있는 최단 거리 유형이다.
# visited[x][y][broken]처럼 좌표와 상태를 함께 방문 처리한다.
# ============================================================
def bfs_break_one_wall(board):
    n = len(board)
    m = len(board[0])
    dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0)])
    dist[0][0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 빈 칸이면 현재 상태 그대로 이동한다.
            if board[nx][ny] == 0 and dist[nx][ny][broken] == -1:
                dist[nx][ny][broken] = dist[x][y][broken] + 1
                queue.append((nx, ny, broken))

            # 벽이고 아직 부순 적이 없으면 broken 상태를 1로 바꿔 이동한다.
            if board[nx][ny] == 1 and broken == 0 and dist[nx][ny][1] == -1:
                dist[nx][ny][1] = dist[x][y][broken] + 1
                queue.append((nx, ny, 1))

    return -1


# ============================================================
# 2. BFS + 비트마스크
# 열쇠와 문이 있는 미로에서 현재 가진 열쇠 상태를 mask로 저장한다.
# ============================================================
def key_door_bfs(board):
    n = len(board)
    m = len(board[0])
    start = None

    for i in range(n):
        for j in range(m):
            if board[i][j] == "S":
                start = (i, j)

    visited = [[[False] * (1 << 6) for _ in range(m)] for _ in range(n)]
    queue = deque([(start[0], start[1], 0, 0)])
    visited[start[0]][start[1]][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, key_mask, dist = queue.popleft()

        if board[x][y] == "E":
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            cell = board[nx][ny]

            if cell == "#":
                continue

            next_mask = key_mask

            # 소문자는 열쇠이므로 해당 비트를 켠다.
            if "a" <= cell <= "f":
                next_mask |= 1 << (ord(cell) - ord("a"))

            # 대문자는 문이므로 대응하는 열쇠가 없으면 지나갈 수 없다.
            if "A" <= cell <= "F":
                need = 1 << (ord(cell) - ord("A"))
                if not (key_mask & need):
                    continue

            if not visited[nx][ny][next_mask]:
                visited[nx][ny][next_mask] = True
                queue.append((nx, ny, next_mask, dist + 1))

    return -1


# ============================================================
# 3. BFS + 멀티 소스 + 시뮬레이션
# 불이 먼저 번지고 사람이 그 시간을 피해서 탈출하는 유형이다.
# ============================================================
def fire_escape(board):
    n = len(board)
    m = len(board[0])
    fire_time = [[-1] * m for _ in range(n)]
    person_time = [[-1] * m for _ in range(n)]
    fire_queue = deque()
    person_queue = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == "F":
                fire_time[i][j] = 0
                fire_queue.append((i, j))
            elif board[i][j] == "J":
                person_time[i][j] = 0
                person_queue.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while fire_queue:
        x, y = fire_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] != "#" and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

    while person_queue:
        x, y = person_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 격자 밖으로 나가면 탈출 성공이다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return person_time[x][y] + 1

            if board[nx][ny] == "#" or person_time[nx][ny] != -1:
                continue

            next_time = person_time[x][y] + 1

            # 불이 도착하지 않거나, 사람이 더 빨리 도착하는 칸만 이동한다.
            if fire_time[nx][ny] == -1 or next_time < fire_time[nx][ny]:
                person_time[nx][ny] = next_time
                person_queue.append((nx, ny))

    return "IMPOSSIBLE"


# ============================================================
# 4. 이분 탐색 + 그래프 판정
# "최대 높이/비용/차이를 최소화"하는 경로 문제에서 자주 쓴다.
# ============================================================
def can_reach_with_limit(board, limit):
    n = len(board)
    m = len(board[0])

    if board[0][0] > limit:
        return False

    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and board[nx][ny] <= limit:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return False


def min_possible_max_cell(board):
    left = max(board[0][0], board[-1][-1])
    right = max(max(row) for row in board)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid 이하의 칸만 밟아서 도착할 수 있으면 더 작은 답을 찾아본다.
        if can_reach_with_limit(board, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


# ============================================================
# 5. 다익스트라 + 상태
# 도로 포장, 쿠폰, 무료 이용권처럼 특수 행동을 한 번 쓸 수 있는 유형이다.
# ============================================================
def dijkstra_with_one_coupon(graph, start, n):
    INF = 10**18
    dist = [[INF] * 2 for _ in range(n + 1)]
    heap = [(0, start, 0)]
    dist[start][0] = 0

    while heap:
        current_cost, now, used = heapq.heappop(heap)

        if current_cost > dist[now][used]:
            continue

        for next_v, cost in graph[now]:
            normal_cost = current_cost + cost

            if normal_cost < dist[next_v][used]:
                dist[next_v][used] = normal_cost
                heapq.heappush(heap, (normal_cost, next_v, used))

            # 쿠폰을 아직 쓰지 않았다면 이번 간선 비용을 0으로 처리한다.
            if used == 0 and current_cost < dist[next_v][1]:
                dist[next_v][1] = current_cost
                heapq.heappush(heap, (current_cost, next_v, 1))

    return dist


# ============================================================
# 6. 최단 경로 + 간선 개수 제한 DP
# 최대 k개의 간선만 사용 가능할 때는 DP식 벨만-포드로 풀 수 있다.
# ============================================================
def cheapest_path_with_k_edges(n, edges, start, target, k):
    INF = 10**18
    dp = [[INF] * (n + 1) for _ in range(k + 2)]
    dp[0][start] = 0

    for used_edges in range(1, k + 2):
        # 간선을 덜 쓰고 도착한 비용도 유지해야 한다.
        for node in range(1, n + 1):
            dp[used_edges][node] = dp[used_edges - 1][node]

        for a, b, cost in edges:
            if dp[used_edges - 1][a] == INF:
                continue

            dp[used_edges][b] = min(
                dp[used_edges][b],
                dp[used_edges - 1][a] + cost
            )

    if dp[k + 1][target] == INF:
        return -1
    return dp[k + 1][target]


# ============================================================
# 7. 위상 정렬 + DP
# DAG에서 가장 긴 경로, 작업 완료 시간, 선수 과목 문제에 사용한다.
# ============================================================
def longest_path_in_dag(n, graph, indegree):
    queue = deque()
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        for next_v, cost in graph[now]:
            # now까지의 최댓값에 간선 비용을 더해 next_v의 최댓값을 갱신한다.
            dp[next_v] = max(dp[next_v], dp[now] + cost)
            indegree[next_v] -= 1

            if indegree[next_v] == 0:
                queue.append(next_v)

    return dp


# ============================================================
# 8. Union-Find + 정렬 + 오프라인 쿼리
# "비용 limit 이하의 간선만 써서 연결 가능한가?" 같은 질문을 빠르게 처리한다.
# ============================================================
def offline_connectivity_queries(n, edges, queries):
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            parent[root_b] = root_a

    edges.sort(key=lambda x: x[2])
    indexed_queries = []

    for index, (limit, a, b) in enumerate(queries):
        indexed_queries.append((limit, a, b, index))

    indexed_queries.sort()
    answer = [False] * len(queries)
    edge_index = 0

    for limit, a, b, query_index in indexed_queries:
        # 현재 limit 이하의 간선은 모두 미리 합쳐 둔다.
        while edge_index < len(edges) and edges[edge_index][2] <= limit:
            x, y, _ = edges[edge_index]
            union(x, y)
            edge_index += 1

        answer[query_index] = find(a) == find(b)

    return answer


# ============================================================
# 9. MST + 그리디
# 도시를 두 그룹으로 나누는 문제는 MST에서 가장 비싼 간선 하나를 빼면 된다.
# ============================================================
def split_city_with_mst(n, edges):
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        parent[root_b] = root_a
        return True

    edges.sort(key=lambda x: x[2])
    total = 0
    max_selected_edge = 0

    for a, b, cost in edges:
        if union(a, b):
            total += cost
            max_selected_edge = max(max_selected_edge, cost)

    return total - max_selected_edge


# ============================================================
# 10. 누적합 + 해시
# 음수가 섞여 있어 투 포인터가 안 될 때도 구간합 K 개수를 셀 수 있다.
# ============================================================
def count_subarray_sum_k(arr, k):
    count = defaultdict(int)
    count[0] = 1
    prefix = 0
    answer = 0

    for value in arr:
        prefix += value

        # prefix - old_prefix == k 이면 old_prefix == prefix - k 이다.
        answer += count[prefix - k]
        count[prefix] += 1

    return answer


# ============================================================
# 11. 슬라이딩 윈도우 + Counter
# 서로 다른 문자가 k개 이하인 가장 긴 부분 문자열 길이를 구한다.
# ============================================================
def longest_substring_at_most_k_distinct(s, k):
    counter = Counter()
    left = 0
    answer = 0

    for right, ch in enumerate(s):
        counter[ch] += 1

        while len(counter) > k:
            counter[s[left]] -= 1

            if counter[s[left]] == 0:
                del counter[s[left]]

            left += 1

        answer = max(answer, right - left + 1)

    return answer


# ============================================================
# 12. 이분 탐색 + 그리디
# 공유기 설치처럼 "최소 거리를 최대화"하는 유형이다.
# ============================================================
def install_router(positions, router_count):
    positions.sort()
    left = 1
    right = positions[-1] - positions[0]
    answer = 0

    def can_install(distance):
        count = 1
        last_position = positions[0]

        for position in positions[1:]:
            if position - last_position >= distance:
                count += 1
                last_position = position

        return count >= router_count

    while left <= right:
        mid = (left + right) // 2

        # mid 거리로 설치 가능하면 더 큰 거리를 시도한다.
        if can_install(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


# ============================================================
# 13. 정렬 + heap
# 강의실 배정처럼 현재 끝나는 시간이 가장 빠른 강의실을 재사용한다.
# ============================================================
def minimum_classrooms(intervals):
    intervals.sort()
    heap = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)


# ============================================================
# 14. DP + 비트마스크
# 외판원 순회 TSP처럼 방문한 집합을 상태로 저장한다.
# ============================================================
def tsp_bitmask(cost):
    n = len(cost)
    INF = 10**18
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for now in range(n):
            if dp[mask][now] == INF:
                continue

            for next_v in range(n):
                if mask & (1 << next_v):
                    continue

                if cost[now][next_v] == 0:
                    continue

                next_mask = mask | (1 << next_v)
                dp[next_mask][next_v] = min(
                    dp[next_mask][next_v],
                    dp[mask][now] + cost[now][next_v]
                )

    answer = INF
    full_mask = (1 << n) - 1

    for last in range(n):
        if cost[last][0] != 0:
            answer = min(answer, dp[full_mask][last] + cost[last][0])

    return answer


# ============================================================
# 15. 백트래킹 + 거리 계산
# 치킨 배달처럼 조합을 고른 뒤 각 집까지의 최소 거리를 계산한다.
# ============================================================
def chicken_distance(city, m):
    houses = []
    chickens = []
    n = len(city)

    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))

    answer = math.inf
    selected = []

    def dfs(index):
        nonlocal answer

        if len(selected) == m:
            total = 0

            for hx, hy in houses:
                # 선택된 치킨집 중 가장 가까운 거리만 더한다.
                total += min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected)

            answer = min(answer, total)
            return

        if index == len(chickens):
            return

        # 현재 치킨집을 선택하는 경우
        selected.append(chickens[index])
        dfs(index + 1)
        selected.pop()

        # 현재 치킨집을 선택하지 않는 경우
        dfs(index + 1)

    dfs(0)
    return answer


# ============================================================
# 16. DFS/BFS + DP 메모이제이션
# 그래프처럼 이동하지만 경로 수를 세야 할 때 사용한다.
# ============================================================
def downhill_path_count(board):
    n = len(board)
    m = len(board[0])
    dp = [[-1] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return 1

        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 높이가 낮은 칸으로만 이동해야 하므로 DAG처럼 생각할 수 있다.
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)

        return dp[x][y]

    return dfs(0, 0)


# ============================================================
# 시험용 복합 유형 판단 기준
# ============================================================
# 1. visited가 2차원이면 부족해 보인다
#    -> BFS/DFS + 상태, 비트마스크, 벽 부수기, 열쇠, 레버
#
# 2. "정답을 X라고 할 때 가능한가?"로 바꿀 수 있다
#    -> 이분 탐색 + BFS/DFS/그리디 판정
#
# 3. "선행 조건을 만족해야 다음으로 간다"
#    -> 위상 정렬 + DP
#
# 4. "최단 경로인데 특수 행동을 K번 쓸 수 있다"
#    -> 다익스트라/BFS + 상태 차원 추가
#
# 5. "간선을 비용순으로 보면서 질문에 답한다"
#    -> 정렬 + Union-Find 오프라인 처리
#
# 6. "구간합인데 음수가 있다"
#    -> 투 포인터가 아니라 누적합 + 해시
#
# 7. "가장 빨리 끝나는 것 재사용"
#    -> 정렬 + heap
#
# 8. "방문한 집합 자체가 상태다"
#    -> 비트마스크 + BFS 또는 DP
#
# 9. "격자를 움직이는데 경로 개수를 센다"
#    -> DFS/BFS 탐색 + DP 메모이제이션
# ============================================================


if __name__ == "__main__":
    wall_board = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print("벽 부수기 BFS:", bfs_break_one_wall(wall_board))

    positions = [1, 2, 8, 4, 9]
    print("공유기 설치:", install_router(positions, 3))

    intervals = [(1, 3), (2, 4), (3, 5)]
    print("강의실:", minimum_classrooms(intervals))
