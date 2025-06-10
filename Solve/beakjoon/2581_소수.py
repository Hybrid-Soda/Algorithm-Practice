# 2581 소수 / 수학, 정수론, 소수 판정

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

m = max(2, int(input()))
n = int(input())
nums = [i for i in range(m, n+1) if isPrime(i)]

if len(nums) < 1:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))