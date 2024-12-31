# 1939 중량제한 / 자료 구조, 그래프 이론, 그래프 탐색, 이분 탐색, 너비 우선 탐색, 최단 경로, 분리 집합

from collections import deque

# 주어진 중량으로 f1에서 f2로 이동 가능한지 확인
def bfs(max_weight, f1, f2, graph):
    queue = deque([f1])
    visit = [0] * len(graph)
    visit[f1] = 1

    while queue:
        now = queue.popleft()
        for next, weight in graph[now]:

            # 방문하지 않았고, 중량이 max_weight 이상인 경우
            if not visit[next] and weight >= max_weight:
                if next == f2: return True
                queue.append(next)
                visit[next] = 1

    return False

# 이진 탐색을 사용하여 가능한 최대 중량을 찾음
def binary_search(start, end, f1, f2, graph):
    ans = 0

    # 중량이 mid일 때 f1에서 f2로 이동 가능한지 확인
    while start <= end:
        mid = (start + end) // 2
        res = bfs(mid, f1, f2, graph)
        if res:
            start = mid + 1
            ans = max(ans, mid)
        else:
            end = mid - 1

    return ans

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    min_w, max_w = float('inf'), 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        min_w = min(min_w, c)
        max_w = max(max_w, c)

    f1, f2 = map(int, input().split())
    print(binary_search(min_w, max_w, f1, f2, graph))

if __name__ == '__main__':
    main()