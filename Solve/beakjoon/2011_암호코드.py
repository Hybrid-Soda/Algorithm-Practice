# 2011 암호코드 / 다이나믹 프로그래밍

code = input()
n = len(code)

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    if code[i-1] != '0':
        dp[i] += dp[i-1]
    if i > 1 and '10' <= code[i-2:i] <= '26':
        dp[i] += dp[i-2]

print(dp[n]%1000000)