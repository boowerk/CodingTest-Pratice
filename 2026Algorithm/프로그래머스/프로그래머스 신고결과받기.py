def solution(id_list, report, k):
    answer = [0] * len(id_list)

    user_index = {user: i for i, user in enumerate(id_list)}
    
    report = set(report)

    reported_by = {user: [] for user in id_list}

    for r in report:
        reporter, reported = r.split()
        reported_by[reported].append(reporter)

    for reported, reporters, in reported_by.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[user_index[reporter]] += 1
    return answer