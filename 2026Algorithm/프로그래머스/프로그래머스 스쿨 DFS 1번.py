# 라이언의 화살 배치를 DFS로 모두 탐색하는 백트래킹 풀이
def solution(n, info):
    best_diff = -1
    best = [-1]

    def calc_diff(ryan):
        apeach_score = 0
        ryan_score = 0

        for i in range(11):
            score = 10 - i
            if info[i] == 0 and ryan[i] == 0:
                continue
            # 같은 점수 칸이면 어피치가 점수를 가져간다.
            if ryan[i] > info[i]:
                ryan_score += score
            else:
                apeach_score += score

        return ryan_score - apeach_score

    def is_better(candidate, current):
        # 점수 차가 같다면 낮은 점수 칸에 더 많이 쏜 배치를 우선한다.
        for i in range(10, -1, -1):
            if candidate > current[i]:
                return True
            elif candidate < current[i]:
                return False
        return False

    def dfs(idx, arrows_left, ryan):
        nonlocal best_diff, best

        if idx == 10:
            # 마지막 0점 칸에 남은 화살을 몰아 넣고 결과를 평가한다.
            ryan[10] = arrows_left
            diff = calc_diff(ryan)

            if diff > best_diff:
                best_diff = diff
                best = ryan[:]
            elif diff == best_diff and is_better(ryan, best):
                best = ryan[:]

            ryan[10] = 0
            return

        need = info[idx] + 1

        if arrows_left >= need:
            # 현재 점수 칸을 이기기 위해 필요한 최소 화살 수를 배치한다.
            ryan[idx] = need
            dfs(idx + 1, arrows_left - need, ryan)
            ryan[idx] = 0

        # 현재 점수 칸을 포기하는 경우도 함께 탐색한다.
        dfs(idx + 1, arrows_left, ryan)

    dfs(0, n, [0]* 11)
    return best
