from collections import deque
import heapq

# ============================================================
# 실전용 Python 기타 그래프 이론 정리
# 핵심:
# 1. 연결 여부 묶기는 Union-Find
# 2. 최소 신장 트리는 Kruskal 또는 Prim
# 3. 선후 관계는 위상 정렬
# 4. 색을 나눌 수 있는지는 이분 그래프
# 5. 트리는 부모, 깊이, 서브트리 크기를 자주 구한다.
# ============================================================


# ============================================================
# 1. Union-Find 기본
# 서로소 집합, 연결 여부, 친구 네트워크, 사이클 판정에 사용한다.
# ============================================================
def find_parent(parent, x):
    if parent[x] != x:
        # 경로 압축으로 다음 탐색을 빠르게 만든다.
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a == root_b:
        return False

    # 번호가 작은 루트를 대표로 삼는 기본 방식이다.
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True


def is_same_set(parent, a, b):
    return find_parent(parent, a) == find_parent(parent, b)


# ============================================================
# 2. Union-Find + 크기 관리
# 집합의 크기, 네트워크 인원 수가 필요할 때 사용한다.
# ============================================================
def union_with_size(parent, size, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a == root_b:
        return size[root_a]

    # 큰 집합에 작은 집합을 붙이면 트리가 깊어지는 것을 줄일 수 있다.
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return size[root_a]


# ============================================================
# 3. Kruskal 최소 신장 트리 MST
# 모든 노드를 최소 비용으로 연결할 때 사용한다.
# ============================================================
def kruskal(n, edges):
    parent = [i for i in range(n + 1)]
    total_cost = 0
    selected_count = 0

    # 비용이 작은 간선부터 고르되, 사이클이 생기면 건너뛴다.
    edges.sort(key=lambda x: x[2])

    for a, b, cost in edges:
        if union_parent(parent, a, b):
            total_cost += cost
            selected_count += 1

            if selected_count == n - 1:
                break

    if selected_count != n - 1:
        return -1
    return total_cost


# ============================================================
# 4. Prim 최소 신장 트리 MST
# 인접 리스트가 주어졌을 때 heap으로 확장한다.
# ============================================================
def prim(n, graph, start=1):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    total_cost = 0
    selected_count = 0

    while heap:
        cost, now = heapq.heappop(heap)

        if visited[now]:
            continue

        visited[now] = True
        total_cost += cost
        selected_count += 1

        for next_v, next_cost in graph[now]:
            if not visited[next_v]:
                heapq.heappush(heap, (next_cost, next_v))

    if selected_count != n:
        return -1
    return total_cost


# ============================================================
# 5. 위상 정렬
# 선수 과목, 작업 순서, 줄 세우기처럼 방향성 선후 관계가 있을 때 사용한다.
# ============================================================
def topological_sort(n, graph, indegree):
    queue = deque()
    order = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        order.append(now)

        for next_v in graph[now]:
            indegree[next_v] -= 1

            if indegree[next_v] == 0:
                queue.append(next_v)

    # 모든 노드를 처리하지 못했다면 사이클이 있는 방향 그래프다.
    if len(order) != n:
        return []

    return order


# ============================================================
# 6. 위상 정렬 + DP
# 각 작업의 선행 작업을 모두 끝낸 뒤 최소 완료 시간을 구한다.
# ============================================================
def topology_with_time(n, graph, indegree, time):
    queue = deque()
    result = time[:]

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        for next_v in graph[now]:
            # next_v는 now가 끝난 뒤에 시작할 수 있으므로 완료 시간을 갱신한다.
            result[next_v] = max(result[next_v], result[now] + time[next_v])
            indegree[next_v] -= 1

            if indegree[next_v] == 0:
                queue.append(next_v)

    return result


# ============================================================
# 7. 이분 그래프 판별
# 인접한 노드끼리 서로 다른 색으로 칠할 수 있는지 확인한다.
# ============================================================
def is_bipartite(n, graph):
    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != 0:
            continue

        queue = deque([start])
        color[start] = 1

        while queue:
            now = queue.popleft()

            for next_v in graph[now]:
                if color[next_v] == 0:
                    color[next_v] = -color[now]
                    queue.append(next_v)

                elif color[next_v] == color[now]:
                    return False

    return True


# ============================================================
# 8. 무방향 그래프 사이클 판정
# Union-Find를 쓰면 간단하게 확인할 수 있다.
# ============================================================
def has_cycle_undirected(n, edges):
    parent = [i for i in range(n + 1)]

    for a, b in edges:
        if find_parent(parent, a) == find_parent(parent, b):
            return True

        union_parent(parent, a, b)

    return False


# ============================================================
# 9. 방향 그래프 사이클 판정 DFS
# state: 0 미방문, 1 현재 탐색 중, 2 탐색 완료
# ============================================================
def has_cycle_directed(n, graph):
    state = [0] * (n + 1)

    def dfs(node):
        state[node] = 1

        for next_v in graph[node]:
            if state[next_v] == 1:
                return True

            if state[next_v] == 0 and dfs(next_v):
                return True

        state[node] = 2
        return False

    for i in range(1, n + 1):
        if state[i] == 0 and dfs(i):
            return True

    return False


# ============================================================
# 10. 트리 부모, 깊이 구하기
# 루트가 주어진 트리에서 parent와 depth 배열을 만든다.
# ============================================================
def get_tree_parent_depth(n, tree, root=1):
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    queue = deque([root])
    parent[root] = -1

    while queue:
        now = queue.popleft()

        for next_v in tree[now]:
            if next_v == parent[now]:
                continue

            parent[next_v] = now
            depth[next_v] = depth[now] + 1
            queue.append(next_v)

    return parent, depth


# ============================================================
# 11. 서브트리 크기
# 트리 DP, 회사 조직도, 칭찬 전파, subtree query에서 자주 사용한다.
# ============================================================
def get_subtree_size(n, tree, root=1):
    parent = [0] * (n + 1)
    order = [root]
    parent[root] = -1

    for now in order:
        for next_v in tree[now]:
            if next_v == parent[now]:
                continue

            parent[next_v] = now
            order.append(next_v)

    size = [1] * (n + 1)

    # 자식부터 부모로 누적해야 하므로 방문 순서를 거꾸로 본다.
    for node in reversed(order[1:]):
        size[parent[node]] += size[node]

    return size


# ============================================================
# 12. LCA 기본
# 두 노드의 가장 가까운 공통 조상을 구한다.
# ============================================================
def prepare_lca(n, tree, root=1):
    LOG = (n).bit_length()
    parent = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    queue = deque([root])
    parent[0][root] = 0

    while queue:
        now = queue.popleft()

        for next_v in tree[now]:
            if next_v == parent[0][now]:
                continue

            parent[0][next_v] = now
            depth[next_v] = depth[now] + 1
            queue.append(next_v)

    for k in range(1, LOG):
        for node in range(1, n + 1):
            parent[k][node] = parent[k - 1][parent[k - 1][node]]

    return parent, depth


def lca(a, b, parent, depth):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]

    # 깊이가 더 깊은 노드를 위로 올려 두 노드의 깊이를 맞춘다.
    for k in range(len(parent)):
        if diff & (1 << k):
            a = parent[k][a]

    if a == b:
        return a

    for k in range(len(parent) - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]


# ============================================================
# 13. SCC - Kosaraju
# 방향 그래프에서 강하게 연결된 컴포넌트를 구한다.
# ============================================================
def kosaraju_scc(n, graph, reverse_graph):
    visited = [False] * (n + 1)
    order = []

    def dfs1(node):
        visited[node] = True

        for next_v in graph[node]:
            if not visited[next_v]:
                dfs1(next_v)

        order.append(node)

    def dfs2(node, component):
        visited[node] = True
        component.append(node)

        for next_v in reverse_graph[node]:
            if not visited[next_v]:
                dfs2(next_v, component)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    visited = [False] * (n + 1)
    components = []

    # 끝나는 시간이 늦은 노드부터 역방향 그래프를 탐색한다.
    for node in reversed(order):
        if not visited[node]:
            component = []
            dfs2(node, component)
            components.append(component)

    return components


# ============================================================
# 시험용 선택 기준
# ============================================================
# 1. "같은 집합인가?", "연결되어 있는가?" -> Union-Find
#
# 2. "모든 섬을 최소 비용으로 연결" -> MST, 보통 Kruskal
#
# 3. "순서가 정해진 작업", "선수 과목" -> 위상 정렬
#
# 4. "팀을 둘로 나누기", "인접한 정점끼리 다른 그룹" -> 이분 그래프
#
# 5. "트리에서 두 노드 사이", "공통 조상" -> 부모/깊이 또는 LCA
#
# 6. 무방향 그래프의 사이클은 Union-Find, 방향 그래프의 사이클은 DFS state나 위상 정렬
#
# 7. MST는 간선이 n - 1개 선택되어야 모든 노드가 연결된 것이다.
# ============================================================


if __name__ == "__main__":
    n = 4
    edges = [(1, 2, 3), (2, 3, 2), (3, 4, 4), (1, 4, 10)]
    print("Kruskal:", kruskal(n, edges))

    graph = [[], [2, 3], [4], [4], []]
    indegree = [0, 0, 1, 1, 2]
    print("Topological:", topological_sort(4, graph, indegree))
