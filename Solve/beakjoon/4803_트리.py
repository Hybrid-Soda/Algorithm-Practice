# 4803 트리 / 자료 구조, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 분리 집합

from collections import deque


def check_tree(node, graph, visited):
    queue = deque([(node, 0)])  # 현재 노드, 부모 노드

    while queue:
        now, parent = queue.popleft()

        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                queue.append((next, now))
            # 이미 방문한 노드가 현재 노드의 부모 노드가 아니면 순환
            elif next != parent:
                return False

    return True


def get_tree_cnt(n, graph):
    tree_cnt = 0
    visited = [0] * (n+1)

    for node in range(1, n+1):
        if not visited[node]:
            visited[node] = 1
            tree_cnt += check_tree(node, graph, visited)

    return tree_cnt


for tc in range(1, int(10e+9)):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    if (n, m) == (0, 0): break

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    tree_cnt = get_tree_cnt(n, graph)

    if tree_cnt <= 0:
        print(f"Case {tc}: No trees.")
    elif tree_cnt == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {tree_cnt} trees.")
