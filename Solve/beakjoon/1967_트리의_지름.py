# 1967 트리의 지름 / 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 트리의 지름

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])

    while queue:
        now = queue.popleft()

        for next, next_d in tree[now]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + next_d

    m = max(visited)
    return [visited.index(m), m]

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, d = map(int,input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

print(bfs(bfs(1)[0])[1])
