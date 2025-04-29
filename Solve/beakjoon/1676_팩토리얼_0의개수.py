# 1676 팩토리얼 0의 개수 / 수학

def facto(n):
    if n > 2:
        return n * facto(n-1)
    else:
        return n

n = int(input())
output = facto(n)
ans = 0

if n == 0:
    exit(print(0))

for i in str(output)[::-1]:
    if i != '0':
        break
    ans += 1

print(ans)

'''
    n = int(input())
    ans = 0

    while n > 1:
        ans += n // 5
        n //= 5

    print(ans)
'''