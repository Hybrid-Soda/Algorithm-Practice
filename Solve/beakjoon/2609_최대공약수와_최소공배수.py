# 2609 최대공약수와 최소공배수 / 수학, 정수론, 유클리드 호제법

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))  # 최대공약수
print(lcm(a, b))  # 최소공배수