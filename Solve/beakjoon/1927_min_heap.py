# 1927 최소 힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(q, x)
    elif x == 0:
        print(heapq.heappop(q) if q else 0)