# 0으로 연결된 칸을 DFS로 묶어서 아이스크림 개수를 세는 풀이
n, m = map(int, input().split())

graph = []

for i in range(n):
    # 한 줄씩 입력받아 얼릴 수 있는 칸(0)과 막힌 칸(1)을 저장한다.
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어나면 현재 탐색을 끝낸다.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        # 방문한 칸은 1로 바꿔 다시 세지 않도록 표시한다.
        graph[x][y] = 1

        dfs(x - 1 , y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        # 하나의 새로운 얼음 덩어리를 찾았다는 뜻이다.
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        # 아직 방문하지 않은 0 영역을 발견할 때마다 정답을 늘린다.
        if dfs(i, j):
            result += 1

print(result)
