from collections import deque
import sys

input = sys.stdin.readline

# ---------------------------------------------------------
# [창작 문제] 얼음 미로 탈출
# ---------------------------------------------------------
# 네가 풀었던 "음료수 얼려 먹기"와 "미로 탈출"을 한 번 꼰 문제다.
#
# [문제 설명]
# N x M 크기의 격자가 주어진다.
# 각 칸은 다음 다섯 종류 중 하나다.
# S : 시작 위치
# E : 도착 위치
# . : 그냥 지나갈 수 있는 길
# # : 절대 지나갈 수 없는 벽
# 0 : 얼음 칸
#
# 캐릭터는 상, 하, 좌, 우로만 이동할 수 있다.
# 벽(#)은 절대 통과할 수 없다.
# 얼음(0)은 원래 통과할 수 없다.
#
# 단, 이동 도중 단 한 번만 "얼음 덩어리 하나"를 녹일 수 있다.
# 여기서 얼음 덩어리란, 상하좌우로 연결된 0들의 집합이다.
# 어떤 얼음 칸에 처음 들어가는 순간,
# 그 칸이 속한 얼음 덩어리 전체가 한 번에 녹아서 길처럼 지나갈 수 있게 된다.
# 이후에는 그 얼음 덩어리에 속한 모든 칸을 자유롭게 이동할 수 있다.
#
# 시작점 S에서 도착점 E까지 가는 최소 이동 칸 수를 구하라.
# 시작 칸과 도착 칸도 칸 수에 포함한다.
# 도달할 수 없다면 -1을 출력한다.
#
# [입력 형식]
# 첫째 줄에 N, M이 주어진다.
# 다음 N개의 줄에 길이 M의 문자열이 주어진다.
#
# [제한]
# 1 <= N, M <= 30
# 격자에는 S와 E가 정확히 하나씩 존재한다.
#
# [출력 형식]
# S에서 E까지 가는 최소 이동 칸 수를 출력한다.
#
# [예시 입력]
# 5 7
# S..#..E
# ##0#0##
# ..000..
# ###.###
# .......
#
# [예시 출력]
# 11
#
# [예시 설명]
# 그냥은 벽과 얼음 때문에 위쪽 길이 끊겨 있다.
# 하지만 가운데 이어진 얼음 덩어리를 한 번 녹이면,
# 그 얼음 덩어리를 통로처럼 사용해서 E까지 11칸 만에 갈 수 있다.
# ---------------------------------------------------------


def label_ice_components(board, n, m):
    # "음료수 얼려 먹기"처럼 0으로 연결된 영역을 같은 번호로 묶는다.
    component = [[0] * m for _ in range(n)]
    component_id = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if board[i][j] != '0' or component[i][j] != 0:
                continue

            component_id += 1
            queue = deque([(i, j)])
            component[i][j] = component_id

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if board[nx][ny] != '0' or component[nx][ny] != 0:
                        continue

                    component[nx][ny] = component_id
                    queue.append((nx, ny))

    return component


def shortest_escape(board, start, end):
    # "미로 탈출"처럼 BFS를 돌리되,
    # 이번에는 "어떤 얼음 덩어리를 녹였는지"까지 상태로 함께 관리한다.
    n = len(board)
    m = len(board[0])
    component = label_ice_components(board, n, m)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    sx, sy = start
    ex, ey = end

    # visited[x][y]에는 이 칸에 도착했을 때 사용한 얼음 덩어리 번호들을 저장한다.
    # 0은 아직 아무 덩어리도 녹이지 않았다는 뜻이다.
    visited = [[set() for _ in range(m)] for _ in range(n)]
    queue = deque([(sx, sy, 0, 1)])
    visited[sx][sy].add(0)

    while queue:
        x, y, melted_id, distance = queue.popleft()

        # BFS이므로 E를 가장 먼저 만난 경로가 곧 최단 경로다.
        if (x, y) == (ex, ey):
            return distance

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            cell = board[nx][ny]

            # 벽은 절대 지나갈 수 없다.
            if cell == '#':
                continue

            next_melted_id = melted_id

            if cell == '0':
                ice_id = component[nx][ny]

                # 아직 아무 얼음 덩어리도 안 녹였다면,
                # 지금 들어가는 얼음 칸의 덩어리를 선택해서 녹인다.
                if melted_id == 0:
                    next_melted_id = ice_id
                # 이미 다른 얼음 덩어리를 녹였다면 이 칸은 지나갈 수 없다.
                elif melted_id != ice_id:
                    continue

            # 같은 칸이라도 어떤 얼음 덩어리를 녹였는지에 따라 이후 경로가 달라진다.
            if next_melted_id in visited[nx][ny]:
                continue

            visited[nx][ny].add(next_melted_id)
            queue.append((nx, ny, next_melted_id, distance + 1))

    return -1


def main():
    # 입력을 읽고 시작점과 도착점을 찾는다.
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]

    start = None
    end = None

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                start = (i, j)
            elif board[i][j] == 'E':
                end = (i, j)

    # 정답을 계산해서 출력한다.
    answer = shortest_escape(board, start, end)
    print(answer)


if __name__ == "__main__":
    main()
