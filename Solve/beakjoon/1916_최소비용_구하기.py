# 1916 최소비용 구하기 / 그래프 이론, 최단 경로, 데이크스트라

from heapq import heappop, heappush

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

start, end = map(int, input().split())

queue = [[0, start]]
dist = [10e9] * (n+1)
dist[start] = 0

while queue:
    now_cost, now = heappop(queue)

    if now == end:
        break

    if dist[now] < now_cost:
        continue

    for next_cost, next in graph[now]:
        cost = now_cost + next_cost

        if dist[next] > cost:
            dist[next] = cost
            heappush(queue, [cost, next])

print(dist[end])