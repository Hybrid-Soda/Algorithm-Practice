# 1568 새 / 수학, 구현

n = int(input())
i = 1
sec = 0

while n > 0:
    if n >= i:
        n -= i
        i += 1
    else:
        n -= 1
        i = 2
    sec += 1

print(sec)