# 2206 벽 부수고 이동하기

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]
dir = ((1, 0), (0, 1), (-1, 0), (0, -1))

queue = [[0, 0, 0]]
while queue:
    w, i, j = queue.popleft()

    if dist[i][j] < w:
        continue

    for di, dj in dir:
        ni, nj = i + di, j + dj

        if 0<=ni<n and 0<=nj<m and not graph[ni][nj]: