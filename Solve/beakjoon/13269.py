N, M = map(int, input().split())
up = [list(map(int, input().split())) for _ in range(N)]
fo = list(map(int, input().split()))
rs = list(map(int, input().split()))
ans = [[0] * M for _ in range(N)]

if max(fo) != max(rs): exit(print(-1))

for i in range(N):
    for j in range(M):
        if up[i][j]:
            ans[i][j] = min(fo[j], rs[N-i-1])

for j in range(M):
    if not any(ans[i][j] == fo[j] for i in range(N)):
        exit(print(-1))
for i in range(N):
    if not any(ans[i][j] == rs[N-i-1] for j in range(M)):
        exit(print(-1))

for i in ans:
    print(*i)