# 2493 탑 / 자료 구조, 스택

n = int(input())
heights = list(map(int, input().split()))
ans = [0] * n
stack = []

# 역방향 탐색 - 남겨진 높은 탑부터 스택에 남겨두는 방법
for i in range(n - 1, -1, -1):
    # 현재 탑과 스택에 있는 탑을 비교 / 현재 탑이 크거나 같으면 신호를 받을 수 있음
    while stack and stack[-1][0] <= heights[i]:
        # 신호를 주는 탑 소모
        height, idx = stack.pop()
        ans[idx] = i + 1

    # 현재 탑을 스택에 추가
    stack.append([heights[i], i])

print(*ans)

# 핵심은 현재 탑의 왼쪽에 있는 같거나 높은 탑을 빠르게 찾는 것

# 순방향 탐색 - 높은 탑부터 스택에 남겨두는 방법
# for i in range(n):
#     # 현재 탑(heights[i])보다 낮은 탑은 신호를 받을 수 없음 -> 제거
#     while stack and stack[-1][0] < heights[i]:
#         stack.pop()
#     # 스택이 비어 있지 않다면, 스택의 맨 위에 있는 탑이 현재 탑의 신호를 받음
#     if stack:
#         ans[i] = stack[-1][1] + 1
#     # 현재 탑을 스택에 추가
#     stack.append((heights[i], i))
# print(*ans)
