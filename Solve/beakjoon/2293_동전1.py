# 2293 동전 1 / 다이나믹 프로그래밍

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        # 현재 금액을 만드는 방법의 수에 이전 금액을 만드는 방법의 수를 더함
        dp[i] += dp[i-coin]

print(dp[-1])