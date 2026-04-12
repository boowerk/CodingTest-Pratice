def solution(number, k):
    stack = []

    for num in number:
        # 더 큰 수를 만들기 위해 이전 작은 값 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)

    # 아직 제거 못한 경우 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)