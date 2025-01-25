# 1890 점프 / 다이나믹 프로그래밍

def dfs(i, j):
    if i == n-1 and j == n-1:
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = 0
    now = board[i][j]

    for di, dj in ((now, 0), (0, now)):
        ni, nj = i + di, j + dj

        if 0<=ni<n and 0<=nj<n:
            dp[i][j] += dfs(ni, nj)
    
    return dp[i][j]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

print(dfs(0, 0))