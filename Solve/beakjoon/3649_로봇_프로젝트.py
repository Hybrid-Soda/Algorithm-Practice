# 3649 로봇 프로젝트 / 정렬, 이분 탐색, 두 포인터

def two_pointer(x: int, n: int, lego: list[int]):
    l1_idx, l2_idx = 0, n-1
    while l1_idx < l2_idx:
        l = lego[l1_idx] + lego[l2_idx]
        if l < x:
            l1_idx += 1
        elif l > x:
            l2_idx -= 1
        else:
            return lego[l1_idx], lego[l2_idx]
    return None, None

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = sorted(int(input()) for _ in range(n))
        l1, l2 = two_pointer(x, n, lego)
        print(f'yes {l1} {l2}' if l2 != None else 'danger')
    except:
        break