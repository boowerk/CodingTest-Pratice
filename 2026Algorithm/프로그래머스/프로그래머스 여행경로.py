from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    # 그래프 만들기
    for a, b in tickets:
        graph[a].append(b)

    # 사전순 정렬
    for key in graph:
        graph[key].sort()

    route = ["ICN"]
    n = len(tickets)

    def dfs(now):
        # 모든 티켓 사용했으면 성공
        if len(route) == n + 1:
            return True

        for i in range(len(graph[now])):
            next_city = graph[now][i]

            if next_city == "": # 이미 사용한 티켓
                continue

            # 티켓 사용 처리
            graph[now][i] = ""
            route.append(next_city)

            if dfs(next_city):
                return True

            # 백트래킹 (되돌리기)
            route.pop()
            graph[now][i] = next_city

        return False

    dfs("ICN")
    return route