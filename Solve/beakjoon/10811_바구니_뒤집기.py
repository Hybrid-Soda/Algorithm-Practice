# 10811 바구니 뒤집기

n, m = map(int, input().split())
basket = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)