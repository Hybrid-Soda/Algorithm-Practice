# 1764 듣보잡 / 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵

n, m = map(int, input().split())

dutdoe = {input(): 0 for _ in range(n)}
ans = 0

for _ in range(m):
    bodoe = input()
    if bodoe in dutdoe:
        dutdoe[bodoe] += 1
        ans += 1

print(ans)
for k, v in sorted(dutdoe.items()):
    if v > 0:
        print(k)