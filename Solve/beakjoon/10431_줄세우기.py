# 10431 줄세우기 / 구현, 정렬, 시뮬레이션

tc = int(input())

for _ in range(tc):
    n, *list = map(int, input().split())
    answer = 0

    for i in range(20):
        for j in range(i):
            if list[i] < list[j]:
                answer += 1
    
    print(n, answer)
