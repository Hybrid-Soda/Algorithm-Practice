# 2206 벽 부수고 이동하기 / 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
dist[0][0][0] = 2

queue = deque([[0, 0, 0]])
while queue:
    i, j, b = queue.popleft()

    # 도착점에 도달하면 종료
    if i == n-1 and j == m-1:
        break

    for di, dj in dir:
        ni, nj = i + di, j + dj
        
        if not (0<=ni<n and 0<=nj<m):
            continue
        
        # 벽을 만났고 아직 벽을 부수지 않은 경우
        if graph[ni][nj] == 1 and b == 0:
            queue.append([ni, nj, 1])
            dist[ni][nj][1] = dist[i][j][0] + 2
        # 벽이 아니고 아직 방문하지 않은 경우
        elif graph[ni][nj] == 0 and dist[ni][nj][b] == float('inf'):
            queue.append([ni, nj, b])
            dist[ni][nj][b] = dist[i][j][b] + 2

min_val = min(dist[n-1][m-1])
if min_val != float('inf'):
    print(min_val//2)
else:
    print(-1)
