# 14658 하늘에서 별똥별이 빗발친다 / 브루트포스 알고리즘

n, m, l, k = map(int, input().split())
star = [tuple(map(int, input().split())) for _ in range(k)]

max_cnt = 0

# 모든 별똥별 x, y 기준의 좌표를 순회
for i in range(k):
    for j in range(k):
        sx = star[i][0]
        sy = star[j][1]

        # 현재 기준점에서 l x l 크기의 영역 내에 있는 별똥별 개수 세기
        cnt = 0
        for x, y in star:
            if sx <= x <= sx + l and sy <= y <= sy + l:
                cnt += 1

        max_cnt = max(max_cnt, cnt)

print(k - max_cnt)
