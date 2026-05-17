n = int(input())

answer = -1

for five in range(n // 5, -1, -1):
    remain = n - five * 5

    if remain % 3 == 0:
        three = remain // 3
        answer = five + three
        break

print(answer)