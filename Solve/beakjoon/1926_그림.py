# 1926 그림

from collections import deque

def bfs(i, j):
    queue = deque([[i, j]])
    picture[i][j] = 0
    area = 1

    while queue:
        i, j = queue.popleft()

        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and picture[ni][nj]:
                queue.append([ni, nj])
                picture[ni][nj] = 0
                area += 1
    
    return area

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
pic_cnt = 0
max_area = 0

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i in range(n):
    for j in range(m):
        if picture[i][j]:
            pic_cnt += 1
            max_area = max(max_area, bfs(i, j))

print(pic_cnt)
print(max_area)