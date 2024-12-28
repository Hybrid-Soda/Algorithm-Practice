# 20444 색종이와 가위

n, k = map(int, input().split())
start, end = 0, n // 2

while start <= end:
    mid = (start + end) // 2
    cnt = (mid + 1) * (n - mid + 1)
    
    if cnt < k:
        start = mid + 1
    elif cnt > k:
        end = mid - 1
    else:
        print("YES")
        quit()

print("NO")