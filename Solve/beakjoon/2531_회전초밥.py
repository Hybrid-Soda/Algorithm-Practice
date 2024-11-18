# 2531 회전 초밥 / 브루트포스 알고리즘, 두 포인터, 슬라이딩 윈도우

n, d, k, c = map(int, input().split())
sushies = [int(input()) for _ in range(n)] * 2
ans = 0

for i in range(n):
    sushi_to_eat = set(sushies[i : i + k] + [c])
    ans = max(ans, len(sushi_to_eat))

print(ans)
