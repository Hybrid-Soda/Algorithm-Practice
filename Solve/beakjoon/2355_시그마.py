# 2355 시그마 / 수학, 사칙연산

def sigma(x):
    return x*(x+1)//2

a, b = map(int, input().split())
if a > b: a, b = b, a
print(sigma(b)-sigma(a-1))