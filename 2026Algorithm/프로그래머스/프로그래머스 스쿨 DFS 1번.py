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
            if ryan[i] > info[i]:
                ryan_score += score
            else:
                apeach_score += score

        return ryan_score - apeach_score

    def is_better(candidate, current):
        for i in range(10, -1, -1):
            if candidate > current[i]:
                return True
            elif candidate < current[i]:
                return False
        return False

    def dfs(idx, arrows_left, ryan):
        nonlocal best_diff, best

        if idx == 10:
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
            ryan[idx] = need
            dfs(idx + 1, arrows_left - need, ryan)
            ryan[idx] = 0

        dfs(idx + 1, arrows_left, ryan)

    dfs(0, n, [0]* 11)
    return best