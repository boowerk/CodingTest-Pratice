n = int(input().strip())
s = input().strip()

points = []   # (row, col, char)
cur = 0
min_row = 10**9
max_row = -10**9

for col, ch in enumerate(s):
    if ch == '+':
        row = cur
        points.append((row, col, '/'))
        cur += 1
    elif ch == '-':
        row = cur - 1
        points.append((row, col, '\\'))
        cur -= 1
    else:  # '='
        row = cur
        points.append((row, col, '_'))

    min_row = min(min_row, row)
    max_row = max(max_row, row)

height = max_row - min_row + 1
board = [['.' for _ in range(n)] for _ in range(height)]

for row, col, ch in points:
    board[max_row - row][col] = ch

for line in board:
    print(''.join(line))