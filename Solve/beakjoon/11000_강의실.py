# 11000 강의실 / 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys, heapq
input = sys.stdin.readline

n = int(input())
time = sorted(list(map(int, input().split())) for _ in range(n))
heap = [time[0][1]]

for i in range(1, n):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))