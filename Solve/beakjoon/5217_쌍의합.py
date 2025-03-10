# 5217 쌍의 합 / 구현

for _ in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}: ", end='')

    for i in range(1, (n-1)//2+1):
        if i < (n-1)//2:
            print(i, n-i, end=', ')
        else:
            print(i, n-i, end='')

    print()