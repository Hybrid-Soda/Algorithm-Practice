# 6064 카잉 달력 / 수학, 브루트포스 알고리즘, 정수론, 중국인의 나머지 정리

import math

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    limit = math.lcm(m, n)
    xx = {i for i in range(x, limit+1, m)}
    yy = {i for i in range(y, limit+1, n)}
    cross = xx&yy

    if cross:
        print(cross.pop())
    else:
        print(-1)