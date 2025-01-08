# 1238 파티 / 그래프 이론, 최단 경로, 데이크스트라

from heapq import heappop, heappush


def dijkstra(target: int, graph: list):
    dist = [float('inf')] * (n+1)
    queue = [[0, target]]
    dist[target] = 0

    while queue:
        w, now = heappop(queue)

        if dist[now] < w:
            continue

        for next, nw in graph[now]:
            if dist[next] > w + nw:
                dist[next] = w + nw
                heappush(queue, [dist[next], next])

    return dist


n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n+1)]  # 정방향 그래프
graph2 = [[] for _ in range(n+1)]  # 역방향 그래프

for _ in range(m):
    s, e, t = map(int, input().split())
    graph1[s].append([e, t])
    graph2[e].append([s, t])

time1 = dijkstra(x, graph1)  # 목적지에서 돌아오는 최단 거리
time2 = dijkstra(x, graph2)  # 목적지로 가는 최단 거리

# 왕복 시간의 최댓값 계산
ans = 0
for i in range(1, n+1):
    ans = max(ans, time1[i] + time2[i])

print(ans)

'''
[다익스트라 함수화 + 그래프 방향 분리]

1. 다익스트라 함수 분리
- 다익스트라 알고리즘을 함수화하여 코드 재사용성을 극대화
- 호출 시 목표 노드와 그래프를 전달하여 정방향 및 역방향 경로를 각각 처리

2. 정방향/역방향 그래프 분리
- 그래프를 정방향과 역방향으로 나눠, 출발지에서 목적지까지의 거리와 목적지에서 출발지까지의 거리를 각각 계산
'''