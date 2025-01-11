# 22866 탑 보기 / 자료 구조, 스택

def check_height(cnt_list, std_idx):
    std_height = heights[std_idx]

    # 스택의 탑이 기준 탑보다 낮거나 같으면 제거
    while stack and stack[-1][0] <= std_height:
        stack.pop()

    if stack:
        o_gap = abs(std_idx - min_ans[i])
        n_gap = abs(std_idx - stack[-1][1])

        # 새로운 거리가 더 짧거나 같으면 최소 거리 갱신
        if o_gap >= n_gap:
            min_ans[i] = stack[-1][1]

    cnt_list[std_idx] = len(stack)
    stack.append([std_height, std_idx])

n = int(input())
heights = list(map(int, input().split()))

increase, decrease = [0] * n, [0] * n
min_ans = [float('inf')] * n

# 오른쪽에서 왼쪽으로 탐색
stack = []
for i in range(n-1, -1, -1):
    check_height(increase, i)

# 왼쪽에서 오른쪽으로 탐색
stack = []
for i in range(n):
    check_height(decrease, i)

for i in range(n):
    cnt = increase[i] + decrease[i]
    if cnt:
        print(cnt, min_ans[i] + 1)
    else:
        print(0)
