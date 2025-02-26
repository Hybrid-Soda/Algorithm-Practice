# 14225 부분수열의 합 / 브루트포스 알고리즘

n = int(input())
s = sorted(map(int, input().split()))
ans = 1

for i in s:
    if i <= ans:
        ans += i

print(ans)