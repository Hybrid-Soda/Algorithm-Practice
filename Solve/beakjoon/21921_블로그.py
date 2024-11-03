# 21921 블로그 / 누적 합, 슬라이딩 윈도우
import sys
sys.stdin = open('input.txt')

N, X = map(int, input().split())
visit = list(map(int, input().split()))
max_visit = 0
max_count = 0

for i in range(N-X+1):
    if i == 0:
        now_visit = sum(visit[:X])
    else:
        now_visit += visit[i+X-1] - visit[i-1]

    if now_visit > max_visit:
        max_visit = now_visit
        max_count = 1
    elif now_visit == max_visit:
        max_count += 1

if max_visit:
    print(max_visit)
    print(max_count)
else:
    print('SAD')