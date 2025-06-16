# 26099 설탕 배달 2 / 수학, 그리디 알고리즘

n = int(input())
cnt = 0

while n % 5 != 0 and n > 0:
    n -= 3
    cnt += 1

if n % 5 == 0:
    cnt += n // 5
else:
    cnt = -1

print(cnt)