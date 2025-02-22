# 1002 터렛 / 수학, 기하학, 많은 조건 분기

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    if dist == 0:
        print(-1 if r1 == r2 else 0)
    else:
        if abs(r1 - r2) < dist < r1 + r2:
            print(2)
        elif abs(r1 - r2) == dist or r1 + r2 == dist:
            print(1)
        else:
            print(0)