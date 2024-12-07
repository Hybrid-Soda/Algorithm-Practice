# 2138 전구와 스위치 / 그리디 알고리즘
import sys

sys.setrecursionlimit(100000)


# def negative_light(now: list[int], idx: int, term: int):
#     for i in range(idx, idx + term):
#         now[i] = 1 - now[i]
#     print(now)


# def dfs(cnt: int, now: list[int], target: list[int]):
#     # print(now)
#     if now == target:
#         return cnt

#     for i in range(n):
#         if i == 0:
#             negative_light(now, i, 2)
#             if now not in visited:
#                 dfs(cnt + 1, now, target)
#                 visited.append(now[:])
#             negative_light(now, i, 2)
#         elif i == n - 1:
#             negative_light(now, i - 1, 2)
#             if now not in visited:
#                 dfs(cnt + 1, now, target)
#                 visited.append(now[:])
#             negative_light(now, i - 1, 2)
#         else:
#             negative_light(now, i - 1, 3)
#             if now not in visited:
#                 dfs(cnt + 1, now, target)
#                 visited.append(now[:])
#             negative_light(now, i - 1, 3)


# n = int(input())
# initial_light = list(map(int, input()))
# target_light = list(map(int, input()))
# visited = [initial_light[:]]
# print(initial_light, target_light)
# print(dfs(0, initial_light, target_light))

n = int(input())
lights = list(map(int, input()))
target = list(map(int, input()))

for i in range(n):
    if lights[i] == target[i]:
        pass
