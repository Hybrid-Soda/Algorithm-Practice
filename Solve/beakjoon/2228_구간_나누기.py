# 2228 구간 나누기 / 다이나믹 프로그래밍

n, m = map(int, input().split())

notcon = [[0] + [-1e9] * m for _ in range(n+1)]
con = [[0] + [-1e9] * m for _ in range(n+1)]

for i in range(1, n+1):
    num = int(input())

    for j in range(1, m+1):
        notcon[i][j] = max(notcon[i-1][j], con[i-1][j])
        con[i][j] = max(notcon[i-1][j-1], con[i-1][j]) + num

print(max(notcon[n][m], con[n][m]))
