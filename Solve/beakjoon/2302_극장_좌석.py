# 2302 극장 좌석 / 다이나믹 프로그래밍

n = int(input())
m = int(input())
fixed = [int(input()) for _ in range(m)]
dp = [1, 1] + [0] * (n-1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
memo = 0

for i in range(n):
    if i+1 in fixed:
        ans *= dp[memo]
        memo = 0
    else:
        memo += 1

ans *= dp[memo]

print(ans)