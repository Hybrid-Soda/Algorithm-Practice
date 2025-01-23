# 2225 합분해 / 수학, 다이나믹 프로그래밍

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1] % 1000000000)