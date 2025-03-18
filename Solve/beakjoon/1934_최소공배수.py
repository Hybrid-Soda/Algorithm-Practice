# 1934 최소공배수 / 수학, 정수론, 유클리드 호제법

from math import gcd

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))
