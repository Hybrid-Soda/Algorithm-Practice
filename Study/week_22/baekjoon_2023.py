# 2023 신기한 소수
N = int(input())

def get_prime(num):
    for i in range(3, int(num**0.5)+1, 2):
        if num%i == 0:
            return 0
    return 1

def find(idx, num):
    if idx == N-1:
        print(num)
        return
    
    for n in [1, 3, 7, 9]:
        if get_prime(num*10+n):
            find(idx+1, num*10+n)

for i in (2, 3, 5, 7):
    find(0, i)