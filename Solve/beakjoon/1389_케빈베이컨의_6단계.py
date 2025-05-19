# 1389 케빈 베이컨의 6단계 / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 플로이드–워셜

n, m = map(int, input().split())
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

min_v = int(1e9)
ans = 0
for i in range(1, n+1):
    s = sum(graph[i][1:])
    if min_v > s:
        min_v = s
        ans = i

print(ans)