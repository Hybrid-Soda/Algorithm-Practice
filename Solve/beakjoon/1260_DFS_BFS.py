# 1260 DFS와 BFS / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from collections import deque


def dfs(now: int, visit: list):
    visit[now] = 1
    print(now, end=" ")

    for next in graph[now]:
        if not visit[next]:
            dfs(next, visit)


def bfs(n: int, v: int):
    queue = deque([v])
    visit = [0] * (n + 1)
    visit[v] = 1

    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for next in graph[now]:
            if not visit[next]:
                queue.append(next)
                visit[next] = 1


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()

dfs(v, [0] * (n + 1))
print()
bfs(n, v)
