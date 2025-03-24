# 10164 격자상의 경로 / 수학, 다이나믹 프로그래밍, 조합론

n, m, k = map(int, input().split())
dp = [[0] * m for _ in range(n)]

if k:
    k -= 1
    oi, oj = k // m, k % m
else:
    oi, oj = n - 1, m - 1

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = 1
        elif (i <= oi and j <= oj):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

for i in range(oi, n):
    for j in range(oj, m):
        if i == oi and j == oj:
            continue
        if i > oi:
            dp[i][j] += dp[i - 1][j]
        if j > oj:
            dp[i][j] += dp[i][j - 1]

print(dp[n - 1][m - 1])