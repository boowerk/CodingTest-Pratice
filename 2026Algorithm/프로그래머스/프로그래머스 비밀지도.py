def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = arr1[i] | arr2[i]
        binary = bin(row)[2:].zfill(n)

        line = ""
        for ch in binary:
            if ch == "1":
                line += "#"
            else:
                line += " "

        answer.append(line)

    return answer