# 2133 타일 채우기

n = int(input())
dp = [1, 0, 3] + [0] * 28

for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * dp[2]
    for j in range(0, i-3, 2):
        dp[i] += dp[j] * 2

print(dp[n])

# n = 2 -> 3
# n = 4 -> 11 / dp[2] * dp[2] + 2
# n = 6 -> 41 / dp[4] * dp[2] + dp[2] * 2 + 2
# n = 8 -> 153 / dp[6] * dp[2] + dp[4] * 2 + dp[2] * 2 + 2