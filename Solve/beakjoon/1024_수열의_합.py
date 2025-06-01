# 1024 수열의 합 / 수학

n, l = map(int, input().split())

for i in range(l, 101):
    x = n/i - (i+1)/2 + 1
    y = int(x)

    if y == x and y >= 0:
        exit(print(*range(y, y+i)))

print(-1)