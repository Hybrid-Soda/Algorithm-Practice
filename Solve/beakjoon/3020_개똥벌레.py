# 3020 개똥벌레 / 이분 탐색, 누적 합

n, h = map(int, input().split())
top = [0] * (h+1)
bottom = [0] * (h+1)

# 종유석과 석순의 높이를 입력받아 각각의 배열에 저장
for i in range(n):
    k = int(input())
    if i % 2 == 0:
        bottom[k] += 1
    else:
        top[k] += 1

# 높이별로 종유석과 석순의 개수를 누적합으로 계산
for i in range(h-1, 0, -1):
    top[i] += top[i+1]
    bottom[i] += bottom[i+1]

min_cnt = 0
min_num = float('inf')

# 각 높이별로 파괴해야 하는 장애물의 수를 계산
for i in range(h):
    obj = top[i+1] + bottom[h-i]
    if obj < min_num:
        min_num = obj
        min_cnt = 1
    elif obj == min_num:
        min_cnt += 1

print(min_num, min_cnt)