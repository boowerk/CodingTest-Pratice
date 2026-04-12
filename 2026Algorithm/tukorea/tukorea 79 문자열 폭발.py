import sys
input = sys.stdin.readline

# 스택의 뒤쪽만 확인하며 폭발 문자열을 즉시 제거하는 풀이
T = input().strip()
remove = input().strip()

stack = []
rlen = len(remove)

for _ in T:
    stack.append(_)
    if len(stack) >= rlen:
        # 방금 넣은 문자 기준으로 뒤쪽 rlen개만 비교하면 된다.
        if ''.join(stack[-rlen:]) == remove:
            for _ in range(rlen):
                stack.pop()

result = ''.join(stack)

# 모두 지워졌으면 0을 출력한다.
print(result if result else 0)
