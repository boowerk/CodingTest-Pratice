import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 비트마스크로 사용한 알파벳 집합을 관리하는 DFS 풀이
R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1

# visited[x][y] = 이 칸에 도착했을 때 나왔던 mask들 저장
visited = [set() for _ in range(R * C)]

def dfs(x, y, mask, depth):
    global answer
    if depth > answer:
        answer = depth
        if answer == 26:   # 알파벳 최대 개수
            print(26)
            sys.exit(0)

    idx = x * C + y
    # 같은 칸에 같은 mask로 다시 왔다면 이후 탐색 결과도 같으므로 중단한다.
    if mask in visited[idx]:
        return
    visited[idx].add(mask)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            # 알파벳 하나를 비트 하나로 표현해 사용 여부를 빠르게 확인한다.
            bit = 1 << (ord(board[nx][ny]) - 65)

            if mask & bit:
                continue

            dfs(nx, ny, mask | bit, depth + 1)

start_mask = 1 << (ord(board[0][0]) - 65)
dfs(0, 0, start_mask, 1)

print(answer)
