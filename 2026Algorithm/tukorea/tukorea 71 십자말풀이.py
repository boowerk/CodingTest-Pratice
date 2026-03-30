A, B = input().split()

row = -1
col = -1

Alen = len(A)
Blen = len(B)

for i in range(Alen):
    found = False
    for j in range(Blen):
        if A[i] == B[j]:
            row = j
            col = i
            found = True
            break
    if found:
        break

for i in range(len(B)):
    if i == row:
        print(A)
    else:
        line = ['.'] * len(A)
        line[col] = B[i]
        print(''.join(line))