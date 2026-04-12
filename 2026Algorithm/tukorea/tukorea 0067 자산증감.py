# 증감 기록을 높이 변화로 바꾼 뒤, 문자 그래프로 그리는 풀이
n = int(input().strip())
s = input().strip()

points = []   # (row, col, char)
cur = 0
min_row = 10**9
max_row = -10**9

for col, ch in enumerate(s):
    if ch == '+':
        # 상승 구간은 현재 높이에서 시작해 '/'로 표시한다.
        row = cur
        points.append((row, col, '/'))
        cur += 1
    elif ch == '-':
        # 하강 구간은 한 칸 아래 높이에서 '\'로 표시한다.
        row = cur - 1
        points.append((row, col, '\\'))
        cur -= 1
    else:  # '='
        # 유지 구간은 현재 높이에서 '_'로 그린다.
        row = cur
        points.append((row, col, '_'))

    min_row = min(min_row, row)
    max_row = max(max_row, row)

height = max_row - min_row + 1
# 최소/최대 높이를 기준으로 필요한 세로 길이만큼 보드를 만든다.
board = [['.' for _ in range(n)] for _ in range(height)]

for row, col, ch in points:
    # 출력은 위에서 아래로 내려오므로 실제 row를 뒤집어 배치한다.
    board[max_row - row][col] = ch

for line in board:
    print(''.join(line))
