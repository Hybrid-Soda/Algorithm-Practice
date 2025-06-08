# 1010 다리 놓기 / 수학, 다이나믹 프로그래밍, 조합론

def bridge(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, m+1):
        dp[1][i] = i

    for i in range(2, n+1):
        for j in range(i, m+1):
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]

    return dp[n][m]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(bridge(n, m))