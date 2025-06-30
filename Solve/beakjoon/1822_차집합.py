# 1822 차집합 / 자료 구조, 정렬, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵

def is_belong(num, arr):
    l, r = 0, nb-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < num:
            l = m + 1
        elif arr[m] > num:
            r = m - 1
        else:
            return True
    return False

na, nb = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
ans = []

for i in a:
    if not is_belong(i, b):
        ans.append(i)

print(len(ans))

if len(ans) != 0:
    print(*ans)