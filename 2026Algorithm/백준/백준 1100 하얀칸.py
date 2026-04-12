# 체스판의 흰 칸 위치만 골라 F의 개수를 세는 풀이
count = 0
# 첫 줄의 첫 칸은 흰 칸이므로 True로 시작한다.
flag = True
for _ in range(8):
    L = input()
    for i in range(8):
        if flag:
            if i % 2 == 0 and L[i] == 'F':
                count += 1
        else:
            if  i % 2 == 1 and L[i] == 'F':
                count += 1
    # 다음 줄은 시작 색이 반대가 되므로 플래그를 뒤집는다.
    flag =  not flag

print(count)
