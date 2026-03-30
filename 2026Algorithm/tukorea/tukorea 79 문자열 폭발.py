import sys
input = sys.stdin.readline

T = input().strip()
remove = input().strip()

stack = []
rlen = len(remove)

for _ in T:
    stack.append(_)
    if len(stack) >= rlen:
        if ''.join(stack[-rlen:]) == remove:
            for _ in range(rlen):
                stack.pop()

result = ''.join(stack)

print(result if result else 0)