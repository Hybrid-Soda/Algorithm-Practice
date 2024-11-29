# 14719 빗물 / 구현, 시뮬레이션

h, w = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    l_max = max(block[:i])
    r_max = max(block[i+1:])
    lower = min(l_max, r_max)
    
    if block[i] < lower:
        ans += lower - block[i]

print(ans)