# 7569 토마토 / 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

m, n, h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                queue.append([i, j, k])

di = [1, 0, 0, -1, 0, 0]
dj = [0, 1, 0, 0, -1, 0]
dk = [0, 0, 1, 0, 0, -1]

while queue:
    i, j, k = queue.popleft()

    for d in range(6):
        ni, nj, nk = i + di[d], j + dj[d], k + dk[d]

        if 0<=ni<h and 0<=nj<n and 0<=nk<m and boxes[ni][nj][nk] == 0:
            queue.append([ni, nj, nk])
            boxes[ni][nj][nk] = boxes[i][j][k] + 1

day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                exit(print(-1))
            day = max(day, boxes[i][j][k])

print(day-1)