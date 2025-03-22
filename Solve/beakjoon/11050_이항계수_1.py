# 11050 이항 계수 1 / 수학, 구현, 조합론

def facto(n):
    if n > 1:
        return n*facto(n-1)
    else:
        return 1

a,b=map(int, input().split())
print(facto(a)//(facto(a-b)*facto(b)))