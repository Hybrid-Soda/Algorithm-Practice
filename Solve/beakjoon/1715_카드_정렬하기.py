# 1715 카드 정렬하기 / 자료 구조, 그리디 알고리즘, 우선순위 큐

from heapq import heappush, heappop

n = int(input())
cards = []
ans = 0

for _ in range(n):
    heappush(cards, int(input()))

while len(cards) > 1:
    hap = heappop(cards) + heappop(cards)
    heappush(cards, hap)
    ans += hap

print(ans)