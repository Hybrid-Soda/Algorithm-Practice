# 1446 지름길 / 다이나믹 프로그래밍, 그래프 이론, 최단 경로, 데이크스트라

n, d = map(int, input().split())
shortcuts = {}
road = [float('inf')] * (d+1)
road[0] = 0

for _ in range(n):
    start, end, length = map(int, input().split())
    shortcuts[start] = shortcuts.setdefault(start, []) + [(end, length)]

for i in range(d+1):
    if i > 0:
        road[i] = min(road[i], road[i-1] + 1)

    if i in shortcuts:
        for end, length in shortcuts[i]:
            if end <= d:
                road[end] = min(road[end], road[i] + length)

print(road[d])