# 11279 최대 힙 / 자료 구조, 우선순위 큐

import heapq

queue = []

for _ in range(int(input())):
    x = int(input())

    if x > 0:
        heapq.heappush(queue, -x)
    else:
        print(-heapq.heappop(queue) if queue else 0)
