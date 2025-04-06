# 11403 경로 찾기 / 그래프 이론, 그래프 탐색, 최단 경로, 플로이드–워셜

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for n in graph:
    print(*n)