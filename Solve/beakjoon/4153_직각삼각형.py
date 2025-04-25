# 4153 직각삼각형 / 수학, 기하학, 피타고라스 정리

while True:
    length = sorted(map(int, input().split()))

    if sum(length) == 0:
        exit()

    if length[0]**2 + length[1]**2 == length[2]**2:
        print('right')
    else:
        print('wrong')