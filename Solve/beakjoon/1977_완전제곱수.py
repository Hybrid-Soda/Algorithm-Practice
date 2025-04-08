# 1977 완전제곱수 / 수학, 구현, 브루트포스 알고리즘

m = int(input())
n = int(input())
sum = 0
min = 0

for i in range(1, 101):
    if m <= i**2 and n >= i**2:
        if sum == 0:
            min = i**2
        sum += i**2

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)