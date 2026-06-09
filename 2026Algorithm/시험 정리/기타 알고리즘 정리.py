from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import heapq
import math

# ============================================================
# 실전용 Python 기타 알고리즘 정리
# 핵심:
# 1. 누적합은 구간 합을 O(1)로 만든다.
# 2. 투 포인터와 슬라이딩 윈도우는 연속 구간 문제에 강하다.
# 3. heap은 매번 최솟값/최댓값이 필요할 때 쓴다.
# 4. stack은 최근 값과 비교해서 제거/매칭할 때 쓴다.
# 5. 좌표 압축, 소수, 조합 계산도 시험에 자주 나온다.
# ============================================================


# ============================================================
# 1. 1차원 누적합
# 구간 [left, right] 합을 빠르게 구한다.
# ============================================================
def prefix_sum_1d(arr):
    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    # arr의 left부터 right까지 합이다. left, right는 0-index 기준이다.
    return prefix[right + 1] - prefix[left]


# ============================================================
# 2. 2차원 누적합
# 직사각형 영역 합을 빠르게 구한다.
# ============================================================
def prefix_sum_2d(board):
    n = len(board)
    m = len(board[0])
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            prefix[y][x] = (
                board[y - 1][x - 1]
                + prefix[y - 1][x]
                + prefix[y][x - 1]
                - prefix[y - 1][x - 1]
            )

    return prefix


def rectangle_sum(prefix, y1, x1, y2, x2):
    # 좌표는 0-index 기준이고, (y1, x1)부터 (y2, x2)까지 포함한다.
    y1 += 1
    x1 += 1
    y2 += 1
    x2 += 1

    return (
        prefix[y2][x2]
        - prefix[y1 - 1][x2]
        - prefix[y2][x1 - 1]
        + prefix[y1 - 1][x1 - 1]
    )


# ============================================================
# 3. 투 포인터
# 양수 배열에서 연속 부분합이 target 이상인 최소 길이를 구한다.
# ============================================================
def min_subarray_len_at_least_target(arr, target):
    answer = math.inf
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        # 조건을 만족하는 동안 왼쪽을 줄여 더 짧은 구간을 찾는다.
        while current_sum >= target:
            answer = min(answer, right - left + 1)
            current_sum -= arr[left]
            left += 1

    if answer == math.inf:
        return 0
    return answer


# ============================================================
# 4. 정렬된 배열 투 포인터
# 두 수의 합이 target에 가장 가까운 쌍을 찾는다.
# ============================================================
def closest_pair_sum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    best_pair = (arr[left], arr[right])
    best_diff = abs(arr[left] + arr[right] - target)

    while left < right:
        current_sum = arr[left] + arr[right]
        current_diff = abs(current_sum - target)

        if current_diff < best_diff:
            best_diff = current_diff
            best_pair = (arr[left], arr[right])

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return best_pair


# ============================================================
# 5. 슬라이딩 윈도우
# 길이가 k인 연속 구간의 최대 합을 구한다.
# ============================================================
def max_window_sum(arr, k):
    if len(arr) < k:
        return 0

    current_sum = sum(arr[:k])
    answer = current_sum

    for right in range(k, len(arr)):
        current_sum += arr[right]
        current_sum -= arr[right - k]
        answer = max(answer, current_sum)

    return answer


# ============================================================
# 6. Counter / 해시
# 빈도수 비교, 완주하지 못한 선수, 애너그램, 신고 결과류에 자주 사용한다.
# ============================================================
def same_frequency(a, b):
    return Counter(a) == Counter(b)


def first_unique_value(arr):
    count = Counter(arr)

    for value in arr:
        if count[value] == 1:
            return value

    return None


# ============================================================
# 7. defaultdict 리스트 그래프/그룹핑
# 키가 없을 때 빈 리스트를 자동으로 만들어준다.
# ============================================================
def group_by_first_char(words):
    groups = defaultdict(list)

    for word in words:
        groups[word[0]].append(word)

    return groups


# ============================================================
# 8. heap 기본
# 매번 가장 작은 값 두 개를 꺼내 섞는 문제에 사용한다.
# ============================================================
def mix_until_target(arr, target):
    heapq.heapify(arr)
    count = 0

    while len(arr) >= 2 and arr[0] < target:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        # 문제 조건에 맞게 새 값을 만들고 다시 heap에 넣는다.
        heapq.heappush(arr, first + second * 2)
        count += 1

    if arr and arr[0] >= target:
        return count
    return -1


# ============================================================
# 9. 최대 heap
# Python heapq는 최소 heap이므로 음수로 넣어 최대 heap처럼 사용한다.
# ============================================================
def max_heap_example(arr):
    heap = []

    for value in arr:
        heapq.heappush(heap, -value)

    result = []
    while heap:
        result.append(-heapq.heappop(heap))

    return result


# ============================================================
# 10. stack - 괄호 검사
# 가장 최근에 열린 괄호부터 닫혀야 하는 구조다.
# ============================================================
def is_valid_parentheses(s):
    stack = []
    pair = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# ============================================================
# 11. stack - 오큰수
# 아직 답을 못 찾은 인덱스를 stack에 넣어둔다.
# ============================================================
def next_greater_element(arr):
    answer = [-1] * len(arr)
    stack = []

    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] < value:
            index = stack.pop()
            answer[index] = value

        stack.append(i)

    return answer


# ============================================================
# 12. 문자열 폭발
# stack 끝부분이 폭발 문자열과 같으면 제거한다.
# ============================================================
def string_explosion(s, bomb):
    stack = []
    bomb_length = len(bomb)

    for ch in s:
        stack.append(ch)

        # 최근에 쌓인 글자들만 확인하면 전체 문자열을 매번 검사하지 않아도 된다.
        if len(stack) >= bomb_length and "".join(stack[-bomb_length:]) == bomb:
            for _ in range(bomb_length):
                stack.pop()

    result = "".join(stack)
    if result:
        return result
    return "FRULA"


# ============================================================
# 13. 좌표 압축
# 값의 크기는 크지만 상대적인 순서만 필요할 때 사용한다.
# ============================================================
def coordinate_compression(arr):
    sorted_values = sorted(set(arr))
    compressed = {value: i for i, value in enumerate(sorted_values)}

    return [compressed[value] for value in arr]


# ============================================================
# 14. 이분 탐색 라이브러리
# lower_bound는 x 이상 첫 위치, upper_bound는 x 초과 첫 위치다.
# ============================================================
def count_by_range(arr, left_value, right_value):
    arr.sort()
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)

    return right_index - left_index


# ============================================================
# 15. 소수 판별
# 한 개의 수가 소수인지 확인한다.
# ============================================================
def is_prime(x):
    if x < 2:
        return False

    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            return False

    return True


# ============================================================
# 16. 에라토스테네스의 체
# 1부터 n까지 소수 목록이 필요할 때 사용한다.
# ============================================================
def sieve(n):
    is_prime_table = [True] * (n + 1)
    is_prime_table[0] = False

    if n >= 1:
        is_prime_table[1] = False

    for num in range(2, int(math.sqrt(n)) + 1):
        if is_prime_table[num]:
            for multiple in range(num * num, n + 1, num):
                is_prime_table[multiple] = False

    return is_prime_table


# ============================================================
# 17. 최대공약수 / 최소공배수
# math.gcd를 쓰면 빠르고 안전하다.
# ============================================================
def gcd_lcm(a, b):
    gcd_value = math.gcd(a, b)
    lcm_value = a * b // gcd_value

    return gcd_value, lcm_value


# ============================================================
# 18. 조합 nCr
# Python 3.8 이상이면 math.comb를 바로 사용할 수 있다.
# ============================================================
def combination_count(n, r):
    if r < 0 or r > n:
        return 0

    return math.comb(n, r)


# ============================================================
# 19. 비트마스크 부분집합
# n이 작을 때 모든 부분집합을 순회한다.
# ============================================================
def bitmask_subsets(arr):
    n = len(arr)
    result = []

    for mask in range(1 << n):
        subset = []

        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])

        result.append(subset)

    return result


# ============================================================
# 20. 비트마스크 방문 처리
# 상태가 작을 때 visited[x][mask] 형태로 쓴다.
# ============================================================
def shortest_visit_all_nodes(graph, start, n):
    full_mask = (1 << n) - 1
    visited = [[False] * (1 << n) for _ in range(n)]
    queue = deque([(start, 1 << start, 0)])
    visited[start][1 << start] = True

    while queue:
        now, mask, dist = queue.popleft()

        if mask == full_mask:
            return dist

        for next_v in graph[now]:
            next_mask = mask | (1 << next_v)

            if not visited[next_v][next_mask]:
                visited[next_v][next_mask] = True
                queue.append((next_v, next_mask, dist + 1))

    return -1


# ============================================================
# 21. KMP 문자열 검색
# 긴 문자열 안에서 패턴이 등장하는 위치를 빠르게 찾는다.
# ============================================================
def build_pi(pattern):
    pi = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi


def kmp_search(text, pattern):
    if not pattern:
        return []

    pi = build_pi(pattern)
    result = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 1)
                j = pi[j]
            else:
                j += 1

    return result


# ============================================================
# 22. 구간 합 + 나머지
# 누적합의 나머지가 같은 두 지점을 고르면 그 사이 합은 m의 배수다.
# ============================================================
def count_subarrays_divisible_by_m(arr, m):
    count = [0] * m
    prefix = 0
    answer = 0
    count[0] = 1

    for value in arr:
        prefix = (prefix + value) % m
        answer += count[prefix]
        count[prefix] += 1

    return answer


# ============================================================
# 시험용 선택 기준
# ============================================================
# 1. "구간 합이 여러 번 필요" -> 누적합
#
# 2. "연속 부분 수열", "구간을 늘리고 줄이기" -> 투 포인터 / 슬라이딩 윈도우
#
# 3. "매번 가장 작은 값", "우선순위" -> heap
#
# 4. "짝 맞추기", "최근 값 제거", "오큰수" -> stack
#
# 5. "빈도수", "중복 개수", "그룹핑" -> Counter / defaultdict
#
# 6. "값의 순위만 필요", "큰 좌표를 작은 인덱스로" -> 좌표 압축
#
# 7. "소수 여러 개" -> 에라토스테네스의 체
#
# 8. "모든 선택 조합이 필요하고 n이 작음" -> DFS 백트래킹 또는 비트마스크
#
# 9. "문자열 패턴 검색" -> KMP 또는 stack 문자열 처리
# ============================================================


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    prefix = prefix_sum_1d(arr)

    print("구간 합:", range_sum(prefix, 1, 3))
    print("최소 길이:", min_subarray_len_at_least_target(arr, 7))
    print("슬라이딩 윈도우:", max_window_sum(arr, 3))
    print("좌표 압축:", coordinate_compression([100, 20, 20, 50]))
    print("KMP:", kmp_search("ababcababd", "ababd"))
