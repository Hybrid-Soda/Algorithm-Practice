# 6198 옥상 정원 꾸미기 / 자료 구조, 스택

n = int(input())
height = [int(input()) for _ in range(n)]
stack = [height[0]]
ans = 0

for i in range(1, n):
    now = height[i]

    while stack and stack[-1] <= now:
        stack.pop()

    ans += len(stack)
    stack.append(now)

print(ans)
