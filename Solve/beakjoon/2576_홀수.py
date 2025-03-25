# 2576 홀수 / 수학, 구현

tot = 0
min_v = 100

for _ in range(7):
    n = int(input())

    if n%2:
        tot += n
        min_v = min(min_v, n)

if tot:
    print(tot)
    print(min_v)
else:
    print(-1)