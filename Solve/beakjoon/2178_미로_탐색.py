# 2178 미로 탐색 / 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    while queue:
        i, j = queue.popleft()
        
        for di, dj in dir:
            ni = i + di
            nj = j + dj

            if 0<=ni<n and 0<=nj<m and miro[ni][nj] == 1:
                miro[ni][nj] = miro[i][j] + 1
                queue.append((ni, nj))

    return miro[n-1][m-1]

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))