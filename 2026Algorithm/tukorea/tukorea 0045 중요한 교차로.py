import sys
sys.setrecursionlimit(10**6)

def find_articulation_points(n, graph):
    order = [0] * (n + 1)   # 방문 순서
    low = [0] * (n + 1)     # low 값
    visited = [False] * (n + 1)
    result = set()

    cnt = 1  # 방문 순서 카운터

    def dfs(node, parent, is_root):
        nonlocal cnt
        visited[node] = True
        order[node] = cnt
        low[node] = cnt
        cnt += 1

        child_count = 0

        for next_node in graph[node]:
            if not visited[next_node]:
                child_count += 1
                dfs(next_node, node, False)

                # 자식 low 값 반영
                low[node] = min(low[node], low[next_node])

                # 루트가 아닌 경우 단절점 조건
                if not is_root and low[next_node] >= order[node]:
                    result.add(node)

            elif next_node != parent:
                # 역방향 간선
                low[node] = min(low[node], order[next_node])

        # 루트 노드 조건
        if is_root and child_count >= 2:
            result.add(node)

    # 모든 노드에서 DFS 시작 (그래프가 끊어져 있을 수도 있음)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1, True)

    return sorted(result)


# --------------------------------------------------
# 입력 처리
# --------------------------------------------------
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# --------------------------------------------------
# 실행
# --------------------------------------------------
result = find_articulation_points(n, graph)

print(len(result))
for x in result:
    print(x)