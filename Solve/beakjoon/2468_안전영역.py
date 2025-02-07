# 2468 안전 영역 / 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque

def bfs(a, b, h, visit):
    q = deque([[a, b]])
    visit[a][b] = 1
 
    while q:
        i, j = q.popleft()
 
        for di, dj in dir:
            ni, nj = i + di, j + dj
            
            if 0<=ni<n and 0<=nj<n and matrix[ni][nj] > h and not visit[ni][nj]:
                visit[ni][nj] = 1
                q.append((ni, nj))

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
n = int(input())
matrix = []
heights = {0}
ans = 0

for _ in range(n):
    temp = list(map(int, input().split()))
    heights.update(set(temp))
    matrix.append(temp)

for h in heights:
    visit = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > h and not visit[i][j]:
                bfs(i, j, h, visit)
                cnt += 1
    
    ans = max(ans, cnt)

print(ans)