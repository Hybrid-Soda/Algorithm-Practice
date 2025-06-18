# 2012 등수 매기기 / 그리디 알고리즘, 정렬

n = int(input())
rank = sorted(int(input()) for _ in range(n))
cnt = 0

for i in range(n):
    if rank[i] != i+1:
        cnt += abs(rank[i]-(i+1))

print(cnt)