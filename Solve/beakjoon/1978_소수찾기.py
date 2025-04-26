# 1978 소수 찾기 / 수학, 정수론, 소수 판정

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in nums:
    if i > 1 and is_prime(i):
        ans += 1

print(ans)