# 9461 파도반 수열

dp = [-1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for _ in range(int(input())):
    n = int(input())

    if dp[n]:
        print(dp[n])
        continue

    for i in range(dp.index(0), n+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n])