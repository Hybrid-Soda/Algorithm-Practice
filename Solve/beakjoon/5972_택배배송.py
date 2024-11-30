# 5972 택배배송 / 그래프 이론, 최단 경로, 데이크스트라

from heapq import heappop, heappush

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

queue = [[0, 1]]
dist = [float("inf")] * (n + 1)
dist[1] = 0

while queue:
    now_cost, now = heappop(queue)

    # 목적지 노드(n)에 도달하면 종료
    if now == n:
        break

    # 이미 처리된 노드라면 건너뜀
    if now_cost > dist[now]:
        continue

    # 현재 노드에서 이동할 수 있는 인접 노드 탐색
    for next_cost, next in graph[now]:

        # 현재 노드를 거쳐 인접 노드로 가는 비용이 더 적다면 업데이트
        if dist[next] > dist[now] + next_cost:
            dist[next] = dist[now] + next_cost
            heappush(queue, [dist[next], next])

print(dist[n])
