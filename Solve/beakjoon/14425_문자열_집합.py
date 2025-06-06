# 14425 문자열 집합 / 자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

n, m = map(int, input().split())
s = set(input() for _ in range(n))
ans = 0

for _ in range(m):
    if input() in s:
        ans += 1

print(ans)