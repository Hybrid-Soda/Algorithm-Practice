# 1806 부분합 / 누적 합, 두 포인터

n, s = map(int, input().split())
serial = list(map(int, input().split()))

start, end = 0, 0
ans = 100001
part_sum = 0

while end <= n:
    if part_sum >= s:
        ans = min(ans, end - start)
        part_sum -= serial[start]
        start += 1
    else:
        if end < n:
            part_sum += serial[end]
        end += 1

print(ans if ans != 100001 else 0)
