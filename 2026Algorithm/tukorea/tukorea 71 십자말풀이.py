# 두 단어에서 처음 만나는 공통 문자를 교차점으로 출력하는 풀이
A, B = input().split()

row = -1
col = -1

Alen = len(A)
Blen = len(B)

for i in range(Alen):
    found = False
    for j in range(Blen):
        # A의 i번째 문자와 B의 j번째 문자가 처음 같아지는 위치를 찾는다.
        if A[i] == B[j]:
            row = j
            col = i
            found = True
            break
    if found:
        break

for i in range(len(B)):
    if i == row:
        # 공통 문자가 있는 행에는 가로 단어 A 전체를 출력한다.
        print(A)
    else:
        line = ['.'] * len(A)
        # 나머지 행에는 교차 열에만 B의 문자를 채운다.
        line[col] = B[i]
        print(''.join(line))
