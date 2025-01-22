# 1520 내리막 길 / 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색

def dfs(i, j):
    # 도착 지점에 도달하면 1을 반환
    if i == m-1 and j == n-1:
        return 1

    # 이미 계산된 경로 수가 있으면 그 값을 반환
    if dp[i][j] != -1:
        return dp[i][j]

    # 경로 수 초기화
    dp[i][j] = 0

    # 네 방향으로 이동
    for di, dj in dir:
        ni, nj = i + di, j + dj

        # 이동할 위치가 범위 내에 있고, 내리막길인 경우
        if 0<=ni<m and 0<=nj<n and arr[ni][nj] < arr[i][j]:
            dp[i][j] += dfs(ni, nj)

    return dp[i][j]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
print(dfs(0, 0))