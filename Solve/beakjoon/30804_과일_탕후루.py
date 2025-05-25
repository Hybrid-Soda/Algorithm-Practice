# 30804 과일 탕후루 / 구현, 브루트포스 알고리즘, 두 포인터

n = int(input())
arr = list(map(int, input().split()))

ans = left = now_var = 0
cnt = {}

for right in range(n):
    rn = arr[right]
    
    if rn in cnt:
        cnt[rn] += 1
    else:
        cnt[rn] = 1
        now_var += 1

    while now_var > 2:
        ln = arr[left]
        cnt[ln] -= 1
        left += 1

        if cnt[ln] == 0:
            cnt.pop(ln)
            now_var -= 1

    ans = max(ans, right - left + 1)

print(ans)