# 13549 숨바꼭질 3 / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색

from heapq import heappop, heappush

n, k = map(int, input().split())
distance = [float('inf')] * 100001
queue = [(0, n)]
distance[n] = 0

while queue:
    dist, now = heappop(queue)

    if distance[now] < dist: continue

    for next in (now-1, now+1, 2*now):
        if not (0 <= next <= 100000): continue

        next_dist = dist if next == 2 * now else dist + 1

        if next_dist < distance[next]:
            if next == k: exit(print(next_dist))

            distance[next] = next_dist
            heappush(queue, (next_dist, next))
