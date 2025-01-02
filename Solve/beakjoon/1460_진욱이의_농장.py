# 1460 진욱이의 농장 / 구현, 다이나믹 프로그래밍, 브루트포스 알고리즘, 이분 탐색, 시뮬레이션, 누적 합

def search_seed(s1, s2):
    dp = [[0] * n for _ in range(n)]

    # 농장에서 s1 또는 s2 씨앗이 있는 위치를 표시
    for i in range(n):
        for j in range(n):
            if farm[i][j] in (s1, s2):
                dp[i][j] = 1
    
    # dp 테이블을 업데이트하여 s1 또는 s2만 포함하는 가장 큰 정사각형 찾기
    for i in range(1, n):
        for j in range(1, n):
            if dp[i][j]:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    
    # 찾은 가장 큰 정사각형의 크기 반환
    return max(map(max, dp))


n, m = map(int, input().split())
farm = [[0] * n for _ in range(n)]
seed = set()

for _ in range(m):
    x, y, l, f = map(int, input().split())
    
    if f:
        seed.add(f)
    
    for i in range(x, x+l):
        for j in range(y, y+l):
            farm[i][j] = f

seed = list(seed)
s = len(seed)
ans = 0

if s == 1:
    ans = search_seed(seed[0], seed[0])
else:
    for i in range(s):
        for j in range(i+1, s):
            ans = max(ans, search_seed(seed[i], seed[j]))

print(ans**2)
