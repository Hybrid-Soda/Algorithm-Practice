# 2143 두 배열의 합 / 자료 구조, 이분 탐색, 누적 합, 해시를 사용한 집합과 맵

t = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

ans = 0
count_a = {}
count_b = {}

# A와 B 배열의 모든 부분합을 계산하여 딕셔너리에 저장
for i in range(n):
    sum_a = 0
    for j in range(i, n):
        sum_a += A[j]
        count_a[sum_a] = count_a.get(sum_a, 0) + 1

for i in range(m):
    sum_b = 0
    for j in range(i, m):
        sum_b += B[j]
        count_b[sum_b] = count_b.get(sum_b, 0) + 1

# 부분합을 조합하여 목표 합을 만드는 경우의 수를 계산
for key in count_a:
    ans += count_a[key] * count_b.get(t - key, 0)

print(ans)