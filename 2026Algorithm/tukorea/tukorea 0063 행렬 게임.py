import sys

input = sys.stdin.readline

A, B = map(int, input().split())

L = []
Left = []
Right = []
Trans = []
num = 1

def rotate_90_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_90_counter_clockwise(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def transpose_board(board):
    return [list(row) for row in zip(*board)]

for _ in range(A):
    row = []
    for _ in range(B):
        row.append(num)
        num += 1
    L.append(row)

if A > 0 and B > 0:
    Left = rotate_90_counter_clockwise(L)
    Right = rotate_90_clockwise(L)
    Trans = transpose_board(L)

print("M")
for row in L:
    print(*row)

print("R")
for row in Right:
    print(*row)

print("L")
for row in Left:
    print(*row)

print("T")
for row in Trans:
    print(*row)
