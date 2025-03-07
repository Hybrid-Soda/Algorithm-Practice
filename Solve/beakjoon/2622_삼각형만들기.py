# 2622 삼각형만들기 / 수학

count = 0
n = int(input())
for i in range(1, n//2 + 1):
    for j in range(i, (n-i)//2 + 1):
        k = n - i - j
        if i + j > k:
            count += 1
print(count)