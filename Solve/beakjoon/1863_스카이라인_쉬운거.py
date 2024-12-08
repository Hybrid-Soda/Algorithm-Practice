# 1863 스카이라인 쉬운거 / 자료 구조, 스택

n = int(input())
stack = []
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        stack.pop()
        cnt += 1

    if not stack or stack[-1] < y:
        stack.append(y)

while stack:
    if stack.pop() > 0:
        cnt += 1

print(cnt)

# 왼쪽 건물부터 순서대로 주어짐 / 단 불연속적
# 이전에 있던 건물의 높이 저장 필요
# 현재까지 나왔던 건물 높이 중 가장 낮은 건물 높이 저장 필요 / 그 위로는 다 제거
# 제거를 어떻게 해야 할까? → 스택
# 예외 상황 : 스택 앞쪽에 뒤보다 더 높은 높이의 건물이 있을 경우 → 건물의 높이가 낮아지는 지점에서 카운트하는 방식으로 변경
