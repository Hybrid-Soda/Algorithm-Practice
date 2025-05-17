# 11726 2xn 타일링 / 다이나믹 프로그래밍

n = int(input())
arr = [0] * 1000
arr[0], arr[1] = 1, 2

for i in range(2, n):
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[n-1] % 10007)