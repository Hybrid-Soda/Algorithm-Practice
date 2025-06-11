# 24313 알고리즘 수업 - 점근적 표기 1 / 수학

def f(n): return a1*n + a0

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(1 if f(n0) <= c*n0 and a1 <= c else 0)