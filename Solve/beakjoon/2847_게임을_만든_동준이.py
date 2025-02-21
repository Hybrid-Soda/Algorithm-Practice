# 2847 게임을 만든 동준이 / 그리디 알고리즘

n = int(input())
score = [int(input()) for _ in range(n)]
ans = 0

for i in range(n-2, -1, -1):
    if score[i+1] <= score[i]:
        sub = score[i] - score[i+1] + 1
        score[i] -= sub
        ans += sub

print(ans)