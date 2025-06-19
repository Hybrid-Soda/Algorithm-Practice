# 17427 약수들의 합 / 수학, 정수론

n = int(input())
ans = 0

for i in range(1, n+1):
    ans += n//i*i

print(ans)