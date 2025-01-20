# 2294 동전 2 / 다이나믹 프로그래밍

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [float('inf')] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[-1] if dp[-1] != float('inf') else -1)