# 10870 피보나치 수 / 수학, 구현

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))