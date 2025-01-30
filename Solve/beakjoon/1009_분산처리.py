# 1009 분산처리 / 수학, 구현

for _ in range(int(input())):
    a, b = map(int, input().split())

    if pow(a, b, 10) == 0:
        print(10)
    else:
        print(pow(a, b, 10))