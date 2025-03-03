# 16566 카드 게임 / 자료 구조, 이분 탐색, 분리 집합

from bisect import bisect_right  

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if y >= m: return
    x, y = find(x), find(y)
    parents[x] = y

n, m, k = map(int, input().split())
cards = sorted(map(int, input().split()))
parents = [i for i in range(m)]

for c in map(int, input().split()):
    idx = bisect_right(cards, c)  # 상대방 카드보다 큰 수 중 최솟값의 위치 찾기
    idx = find(idx)  # 해당 카드의 실제 사용 가능한 위치 찾기
    print(cards[idx])  # 사용할 카드 출력
    union(idx, idx+1)  # 사용한 카드와 다음 카드를 연결