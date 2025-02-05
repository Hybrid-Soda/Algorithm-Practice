# 5014 스타트링크 / 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

f, s, g, u, d = map(int, input().split())
floor = [0] * (f+1)
floor[s] = 1

queue = deque([s])
while queue:
    now = queue.popleft()

    for next in (now+u, now-d):
        if 0<next<=f and not floor[next]:
            queue.append(next)
            floor[next] = floor[now] + 1

print(floor[g] - 1 if floor[g] else "use the stairs")