from collections import deque, defaultdict, Counter

# 구현 문제에서 자주 쓰는 보조 함수와 패턴을 모아둔 정리 파일

# ---------------------------------------------------------
# 1. 방향 배열
# ---------------------------------------------------------
# 상, 하, 좌, 우 이동
dx4 = [-1, 1, 0, 0]
dy4 = [0, 0, -1, 1]

# 대각선 포함 8방향 이동
dx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]

# 방향 인덱스를 쓰는 문제에서 자주 사용
# 0 = 북, 1 = 동, 2 = 남, 3 = 서
dir4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 맨해튼 거리 계산
def manhattan_distance(x1, y1, x2, y2):
    """격자에서 상하좌우 이동 기준 거리"""
    return abs(x1 - x2) + abs(y1 - y2)

# ---------------------------------------------------------
# 2. 범위 체크 함수
# ---------------------------------------------------------
def in_range(x, y, n, m):
    """좌표 (x, y)가 n x m 범위 안에 있으면 True"""
    return 0 <= x < n and 0 <= y < m


# ---------------------------------------------------------
# 3. 문자열 처리 함수들
# ---------------------------------------------------------
def extract_numbers(s):
    """문자열에서 숫자만 뽑아서 int 리스트로 반환"""
    return [int(c) for c in s if c.isdigit()]


def extract_letters(s):
    """문자열에서 알파벳만 뽑아서 리스트로 반환"""
    return [c for c in s if c.isalpha()]


def sort_letters_and_sum_numbers(s):
    """
    문자열에서
    - 알파벳은 정렬
    - 숫자는 모두 더한 뒤 뒤에 붙인다
    예: 'K1KA5CB7' -> 'ABCKK13'
    """
    letters = []
    num_sum = 0

    for c in s:
        if c.isalpha():
            letters.append(c)
        elif c.isdigit():
            num_sum += int(c)

    letters.sort()
    result = ''.join(letters)

    if num_sum > 0:
        result += str(num_sum)

    return result


def reverse_string(s):
    """문자열 뒤집기"""
    return s[::-1]


# ---------------------------------------------------------
# 4. 배열/행렬 회전
# ---------------------------------------------------------
def rotate_90_clockwise(matrix):
    """
    2차원 배열을 시계 방향으로 90도 회전
    반환형은 list of list
    """
    return [list(row) for row in zip(*matrix[::-1])]


def rotate_90_counter_clockwise(matrix):
    """
    2차원 배열을 반시계 방향으로 90도 회전
    """
    return [list(row) for row in zip(*matrix)][::-1]


def transpose_board(board):
    """2차원 배열의 행과 열을 뒤집는다"""
    return [list(row) for row in zip(*board)]


# ---------------------------------------------------------
# 5. 누적합
# ---------------------------------------------------------
def build_prefix_sum(arr):
    """
    1차원 누적합 생성
    prefix[i] = arr[0]부터 arr[i-1]까지의 합
    """
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


def range_sum(prefix, left, right):
    """
    누적합 배열이 있을 때 arr[left:right+1]의 합 반환
    """
    return prefix[right + 1] - prefix[left]


def build_2d_prefix_sum(board):
    """
    2차원 누적합 생성
    prefix[x][y]는 (0,0)부터 (x-1,y-1)까지의 합
    """
    n = len(board)
    m = len(board[0]) if n > 0 else 0
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (
                board[i - 1][j - 1]
                + prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
            )

    return prefix


def range_sum_2d(prefix, x1, y1, x2, y2):
    """
    2차원 누적합으로 (x1,y1)부터 (x2,y2)까지 합을 구한다
    """
    return (
        prefix[x2 + 1][y2 + 1]
        - prefix[x1][y2 + 1]
        - prefix[x2 + 1][y1]
        + prefix[x1][y1]
    )


# ---------------------------------------------------------
# 6. 좌표 이동 함수
# ---------------------------------------------------------
def move_by_command(x, y, cmd):
    """
    문자 명령에 따라 좌표 이동
    U D L R 기준
    """
    move_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    if cmd in move_map:
        dx, dy = move_map[cmd]
        return x + dx, y + dy

    return x, y


# ---------------------------------------------------------
# 7. 방향 회전 함수
# ---------------------------------------------------------
def turn_right(direction):
    """
    방향 회전: 시계 방향
    0=북, 1=동, 2=남, 3=서
    """
    return (direction + 1) % 4


def turn_left(direction):
    """
    방향 회전: 반시계 방향
    0=북, 1=동, 2=남, 3=서
    """
    return (direction - 1) % 4


# ---------------------------------------------------------
# 8. 2차원 배열 출력 함수
# ---------------------------------------------------------
def print_board(board):
    """디버깅용 2차원 배열 출력"""
    for row in board:
        print(*row)
    print()


# ---------------------------------------------------------
# 9. 구현 문제 기본 solution 템플릿
# ---------------------------------------------------------
def solution(data):
    """
    구현 문제 기본 풀이 구조

    [문제에 맞게 수정할 부분]
    1. 입력 데이터 형태
    2. board / 문자열 / 배열 등 실제 사용 변수
    3. 조건 처리
    4. 정답 계산
    """

    # -----------------------------------------------------
    # A. 입력 준비
    # -----------------------------------------------------
    # 예시:
    # board = data
    # s = data
    # arr = data
    #
    # 문제마다 입력 형태에 맞게 바꿔서 사용
    # -----------------------------------------------------
    board = data

    # board가 2차원 배열이라고 가정한 예시
    n = len(board)
    m = len(board[0]) if n > 0 else 0

    # -----------------------------------------------------
    # B. 자주 쓰는 자료구조 준비
    # -----------------------------------------------------
    # 방문 체크용
    visited = [[False] * m for _ in range(n)] if n > 0 else []

    # 카운팅용
    count = defaultdict(int)

    # 좌표 방문 기록용
    visited_positions = set()

    # 정답 변수
    answer = 0

    # -----------------------------------------------------
    # C. 2차원 배열 순회 예시
    # -----------------------------------------------------
    for i in range(n):
        for j in range(m):
            value = board[i][j]

            # 예시: 값 카운팅
            count[value] += 1

            # 예시: 특정 조건 찾기
            if value == 1:
                answer += 1

    # -----------------------------------------------------
    # D. 상하좌우 이동 예시
    # -----------------------------------------------------
    # 시작 좌표 예시
    x, y = 0, 0
    visited_positions.add((x, y))

    # 문제에 따라 명령 문자열이 주어진다고 가정한 예시
    commands = "RRDDLU"

    for cmd in commands:
        # 명령을 좌표 변화로 바꾼 뒤, 범위 안이면 실제 위치를 갱신한다.
        nx, ny = move_by_command(x, y, cmd)

        # 범위 안일 때만 이동
        if in_range(nx, ny, n, m):
            x, y = nx, ny
            visited_positions.add((x, y))

    # -----------------------------------------------------
    # E. 방향 인덱스 기반 이동 예시
    # -----------------------------------------------------
    # direction = 0 -> 북
    direction = 0

    # 오른쪽으로 한 번 회전
    direction = turn_right(direction)

    # 현재 방향으로 1칸 이동
    if n > 0 and m > 0:
        nx = x + dir4[direction][0]
        ny = y + dir4[direction][1]

        if in_range(nx, ny, n, m):
            x, y = nx, ny

    # -----------------------------------------------------
    # F. 4방향 탐색 예시
    # -----------------------------------------------------
    if n > 0 and m > 0:
        for d in range(4):
            nx = x + dx4[d]
            ny = y + dy4[d]

            if not in_range(nx, ny, n, m):
                continue

            # 문제에 맞는 조건 처리
            # 예: board[nx][ny]가 벽인지 확인
            # 예: 주변 칸 개수 세기
            pass

    # -----------------------------------------------------
    # G. 8방향 탐색 예시
    # -----------------------------------------------------
    if n > 0 and m > 0:
        around_count = 0

        for d in range(8):
            nx = x + dx8[d]
            ny = y + dy8[d]

            if not in_range(nx, ny, n, m):
                continue

            # 예시: 주변에 1이 몇 개 있는지 세기
            if board[nx][ny] == 1:
                around_count += 1

    # -----------------------------------------------------
    # H. 문자열 처리 예시
    # -----------------------------------------------------
    s = "K1KA5CB7"

    nums = extract_numbers(s)              # [1, 5, 7]
    letters = extract_letters(s)           # ['K', 'K', 'A', 'C', 'B']
    merged = sort_letters_and_sum_numbers(s)  # ABCKK13
    rev = reverse_string(s)                # 7BC5AK1K

    # -----------------------------------------------------
    # I. 배열 회전 예시
    # -----------------------------------------------------
    if n > 0 and m > 0:
        rotated = rotate_90_clockwise(board)
        # 필요하면 rotated 사용

    # -----------------------------------------------------
    # J. 누적합 예시
    # -----------------------------------------------------
    arr = [1, 2, 3, 4, 5]
    prefix = build_prefix_sum(arr)
    section_sum = range_sum(prefix, 1, 3)  # 2+3+4 = 9

    # -----------------------------------------------------
    # K. 시뮬레이션 구조 예시
    # -----------------------------------------------------
    # 시간, 턴, 단계가 있는 문제에서 자주 사용
    time = 0
    state = 0

    while time < 3:
        # 1. 시간 증가
        time += 1

        # 2. 상태 변화
        state += 1

        # 3. 종료 조건 검사
        if state == 2:
            break

    # -----------------------------------------------------
    # L. 예시 정답 반환
    # -----------------------------------------------------
    # 실제 문제에서는 여기서 문제에서 요구한 값 반환
    return answer


# ---------------------------------------------------------
# 10. 자주 쓰는 별도 패턴 모음
# ---------------------------------------------------------

def count_items(arr):
    """리스트 원소 개수 세기"""
    return Counter(arr)


def find_all_positions(board, target):
    """board에서 target 값이 있는 모든 좌표 반환"""
    n = len(board)
    m = len(board[0])
    result = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == target:
                result.append((i, j))

    return result


def copy_board(board):
    """2차원 배열 깊은 복사"""
    return [row[:] for row in board]


def compress_coordinates(values):
    """좌표 압축 결과를 딕셔너리로 반환"""
    sorted_unique = sorted(set(values))
    return {value: idx for idx, value in enumerate(sorted_unique)}


# ---------------------------------------------------------
# 11. 테스트용 실행
# ---------------------------------------------------------
if __name__ == "__main__":
    sample_board = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    print(solution(sample_board))
    print("맨해튼 거리:", manhattan_distance(0, 0, 2, 3))
    print("전치:", transpose_board(sample_board))

    prefix_2d = build_2d_prefix_sum(sample_board)
    print("2차원 누적합 구간합:", range_sum_2d(prefix_2d, 0, 0, 1, 1))
    print("좌표 압축:", compress_coordinates([50, 10, 50, 20]))
