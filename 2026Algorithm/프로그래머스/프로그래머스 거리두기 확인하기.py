from collections import deque


def solution(places):
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y, place):
        visited = [[False] * 5 for _ in range(5)]
        queue = deque([(x, y, 0)])
        visited[x][y] = True

        while queue:
            x, y, dist = queue.popleft()

            # 거리가 2 이상
            if dist >= 2:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if place[nx][ny] == 'P':
                        return False

                    if place[nx][ny] == 'O':
                        queue.append((nx, ny, dist + 1))

        return True

    for place in places:
        valid = True

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(i, j, place):
                        valid = False
                        break

            if not valid:
                break

        answer.append(1 if valid else 0)

    return answer