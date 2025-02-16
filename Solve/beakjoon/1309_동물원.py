# 1309 동물원 / 다이나믹 프로그래밍

n = int(input())
dp = [1, 3, 7, 17, 41] + [0] * (n-4)

for i in range(5, n+1):
    dp[i] = (dp[i-2] + dp[i-1]*2) % 9901

print(dp[n] % 9901)