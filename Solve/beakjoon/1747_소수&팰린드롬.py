# 1747 소수&팰린드롬 / 수학, 브루트포스 알고리즘, 정수론, 소수 판정, 에라토스테네스의 체

n = int(input())

if n == 1:
    exit(print(2))

for i in range(n, 1000001):
    str_i = str(i)
    
    if str_i != str_i[::-1]:
        continue

    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        exit(print(i))