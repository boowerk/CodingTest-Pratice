import sys
sys.setrecursionlimit(10**6)

# 8방향 DFS로 연결된 땅을 모두 지우면서 섬 개수를 세는 풀이
def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 1:
        # 현재 땅을 바다로 바꿔 같은 섬을 다시 세지 않도록 한다.
        graph[x][y] = 0

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)

        return True
    return False

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []

    for i in range(h):
        graph.append(list(map(int, input().split())))

    result = 0

    for i in range(h):
        for j in range(w):
            # 새로운 섬을 만날 때마다 DFS를 한 번 돌리고 카운트를 올린다.
            if dfs(i, j):
                result += 1

    print(result)
