from collections import defaultdict

# 티켓을 하나씩 소모하며 사전순으로 가장 앞서는 경로를 찾는 DFS 풀이
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

    # 출발지는 항상 ICN으로 고정된다.
    dfs("ICN")
    return route
