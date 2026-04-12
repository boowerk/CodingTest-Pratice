# 손님 번호를 층과 호수로 나눠 실제 방 번호를 계산하는 풀이
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        # 층수로 딱 나누어떨어지면 가장 높은 층에 배정된다.
        floor = H
        room = N // H
    else:
        # 나머지는 층 번호, 몫 + 1은 호수 번호가 된다.
        floor = N % H
        room = N // H + 1

    print(floor * 100 + room)
