# 4485 녹색 옷 입은 애가 젤다지? / 그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라

from heapq import heappop, heappush


def dijkstra(n: int, cave: list[list[int]]) -> int:
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = cave[0][0]
    queue = [[cave[0][0], 0, 0]]

    while True:
        now_cost, i, j = heappop(queue)

        if costs[i][j] < now_cost:
            continue

        for di, dj in dir:
            ni, nj = i + di, j + dj
            
            if 0<=ni<n and 0<=nj<n:
                next_cost = costs[i][j] + cave[ni][nj]

                if ni == n-1 and nj == n-1:
                    return next_cost

                if costs[ni][nj] <= next_cost:
                    continue

                costs[ni][nj] = next_cost
                heappush(queue, [next_cost, ni, nj])


tc = 1
dir = (1, 0), (0, 1), (-1, 0), (0, -1)

while True:
    n = int(input())

    if n == 0: break

    cave = [list(map(int, input().split())) for _ in range(n)]
    ans = dijkstra(n, cave)

    print(f"Problem {tc}: {ans}")
    tc += 1
