# 14940 쉬운 최단거리 / 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

def find_start():
    for i in range(row):
        for j in range(col):
            if ground[i][j] == 2:
                queue.append((i, j, 0))
                ground[i][j] = 0
                return

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
row, col = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(row)]
queue = deque([])

find_start()

while queue:
    i, j, d = queue.popleft()

    for di, dj in dir:
        ni, nj = i + di, j + dj
        
        if 0<=ni<row and 0<=nj<col and ground[ni][nj] == 1:
            queue.append((ni, nj, d+1))
            ground[ni][nj] = f'{d+1}'

for i in range(row):
    for j in range(col):
        print(ground[i][j] if ground[i][j] != 1 else -1, end=' ')
    print()
