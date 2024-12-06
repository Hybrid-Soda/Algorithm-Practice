# 16234 인구 이동 / 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색

from collections import deque


# 국경선을 열 국가 탐색
def bfs(i: int, j: int):
    queue = deque([[i, j]])
    union = [[i, j]]
    population = country[i][j]

    while queue:
        i, j = queue.popleft()
        now = country[i][j]

        for di, dj in dir:
            ni, nj = i + di, j + dj

            if (0<=ni<n and 0<=nj<n
                and l<=abs(now-country[ni][nj])<=r
                and not visited[ni][nj]
                ):
                population += country[ni][nj]
                queue.append([ni, nj])
                union.append([ni, nj])
                visited[ni][nj] = 1

    return union, population


# 인구 이동
def move(union: list[list[int]], population: int):
    union_cnt = len(union)
    new_population = population // union_cnt

    if union_cnt == 1:
        return False
    
    for i, j in union:
        country[i][j] = new_population

    return True


# 메인
n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
dir = (1, 0), (0, 1), (-1, 0), (0, -1)
ans = 0

while True:
    visited = [[0] * n for _ in range(n)]
    flag = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                union, population = bfs(i, j)

                if move(union, population):
                    flag = False
    if flag:
        break
    
    ans += 1

print(ans)
