# 376914 택배 마스터 광우

from itertools import permutations

def run(rail):
    total = 0
    cnt = 0

    for _ in range(k):
        basket = 0
    
        while basket + rail[cnt] <= m:
            basket += rail[cnt]
            cnt = (cnt + 1) % n

        total += basket

    return total

n, m, k = map(int, input().split())
weights = map(int, input().split())
ans = set()

for rail in permutations(weights, n):
    ans.add(run(rail))

print(min(ans))
