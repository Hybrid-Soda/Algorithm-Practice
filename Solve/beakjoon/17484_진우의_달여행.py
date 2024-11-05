# 17484 진우의 달 여행 / 다이나믹 프로그래밍, 브루트포스 알고리즘
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for d in range(3):
        dp[0][j][d] = grid[0][j]

for i in range(1, n):
    for j in range(m):
        if j > 0:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + grid[i][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + grid[i][j]
        if j < m - 1:
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + grid[i][j]

result = min(dp[n-1][j][k] for j in range(m) for k in range(3))
print(result)