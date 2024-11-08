# 3758 KCPC / 구현, 정렬

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())

    # 조건을 따로 저장
    score = [[0] * (k+1) for _ in range(n+1)]
    count = [0] * (n+1)
    order = [0] * (n+1)

    for l in range(m):
        i, j, s = map(int, input().split())

        score[i][j] = max(score[i][j], s)
        count[i] += 1
        order[i] = l
    
    rank = sorted([i for i in range(1, n+1)], key=lambda x: (-sum(score[x]), count[x], order[x]))
    print(rank.index(t)+1)
