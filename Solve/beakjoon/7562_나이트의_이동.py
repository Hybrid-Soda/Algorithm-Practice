# 7562 나이트의 이동 / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 격자 그래프

from collections import deque

dir = (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)

def bfs(l, now_i, now_j, go_i, go_j):
    queue = deque([(now_i, now_j)])
    visit = [[0] * l for _ in range(l)]
    visit[now_i][now_j] = 1

    while queue:
        i, j = queue.popleft()

        if (i, j) == (go_i, go_j):
            return visit[i][j] - 1

        for di, dj in dir:
            ni, nj = i + di, j + dj

            if 0<=ni<l and 0<=nj<l and not visit[ni][nj]:
                if (ni, nj) == (go_i, go_j):
                    return visit[i][j]
        
                queue.append((ni, nj))
                visit[ni][nj] = visit[i][j] + 1


for _ in range(int(input())):
    l = int(input())
    i, j = map(int, input().split())
    ni, nj = map(int, input().split())

    print(bfs(l, i, j, ni, nj))