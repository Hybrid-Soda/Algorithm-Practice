# 2442 별 찍기 - 5 / 구현

n = int(input())

for i in range(1, n+1):
    t = 2*i-1
    b = (2*n-1-t)//2
    print(' '*b + '*'*t)