# 20922 겹치는 건 싫어 / 투 포인터

n, k = map(int, input().split())
serial = list(map(int, input().split()))
check = [0] * 100001
l, r = 0, -1
ans = 0

# 1. 수열의 각 원소 개수 저장
# 2. 1초 -> 브루트 포스 불가능 / 후보 : 투 포인터 (최장 연속 부분 수열 찾기)
for num in serial:
    check[num] += 1
    r += 1

    while check[num] > k:
        l_num = serial[l]
        check[l_num] -= 1
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
