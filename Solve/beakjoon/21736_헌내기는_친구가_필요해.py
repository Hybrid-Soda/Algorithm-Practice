# 21736 헌내기는 친구가 필요해 / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프

from collections import deque

def find_doyeon(campus):
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                return i, j

def bfs(campus):
    go = (1, 0), (0, 1), (-1, 0), (0, -1)
    queue = deque([find_doyeon(campus)])
    visit = [[0] * m for _ in range(n)]
    cnt = 0

    while queue:
        i, j = queue.popleft()
        visit[i][j] = 1

        if campus[i][j] == 'P':
            cnt += 1
        
        for di, dj in go:
            ni, nj = i + di, j + dj

            if 0<=ni<n and 0<=nj<m and campus[ni][nj] != 'X' and not visit[ni][nj]:
                queue.append((ni, nj))
                visit[ni][nj] = 1

    return cnt if cnt else 'TT'

n, m = map(int, input().split())
campus = [input() for _ in range(n)]
print(bfs(campus))