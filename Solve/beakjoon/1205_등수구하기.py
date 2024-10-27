# 1205 등수 구하기 / 구현

n, s, p = map(int, input().split())

# 랭킹 리스트에 점수가 없으면 1등
if not n:
    exit(print(1))

scores = list(map(int, input().split()))

# 랭킹이 꽉 차있고, 최하점보다 크지 않으면 -1 출력 후 종료
if n == p and scores[-1] >= s: 
    exit(print(-1))

# 작거나 같은 점수를 찾아 등수를 결정
for i in range(n):
    if scores[i] <= s:
        exit(print(i+1))

# 점수가 가장 낮은 경우, n+1등
print(n+1)