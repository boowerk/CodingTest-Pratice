import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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
    if mask in visited[idx]:
        return
    visited[idx].add(mask)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            bit = 1 << (ord(board[nx][ny]) - 65)

            if mask & bit:
                continue

            dfs(nx, ny, mask | bit, depth + 1)

start_mask = 1 << (ord(board[0][0]) - 65)
dfs(0, 0, start_mask, 1)

print(answer)