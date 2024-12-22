# 1027 고층 건물 / 수학, 브루트포스 알고리즘, 기하학

N = int(input())
buildings = list(map(int, input().split()))
ans = [0] * N

def get_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def can_see(x1, y1, x2, y2):
    slope = get_slope(x1, y1, x2, y2)
    
    for i in range(x1 + 1, x2):
        if y1 + slope * (i - x1) <= buildings[i]:
            return False
    
    return True

for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if can_see(i, buildings[i], j, buildings[j]):
            ans[i] += 1
            ans[j] += 1

print(max(ans))