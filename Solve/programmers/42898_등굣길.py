def solution(m, n, puddles):
    grid = [[0] * m for _ in range(n)]
    grid[0][0] = 1

    for j, i in puddles:
        grid[i-1][j-1] = -1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                grid[i][j] = 0
                continue
            if i > 0:
                grid[i][j] += grid[i-1][j]
            if j > 0:
                grid[i][j] += grid[i][j-1]

    return grid[n-1][m-1] % 1000000007