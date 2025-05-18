# 1074 Z / 분할 정복, 재귀

def z(n, r, c, res):
    half = 2 ** n // 2
    if n == 1:
        print(2 * r + c + res)
        return

    if r >= half and c >= half:
        z(n - 1, r - half, c - half, res + 3 * half * half)
    elif r >= half > c:
        z(n - 1, r - half, c, res + 2 * half * half)
    elif r < half <= c:
        z(n - 1, r, c - half, res + half * half)
    else:
        z(n - 1, r, c, res)

n, r, c = map(int, input().split())
z(n, r, c, 0)