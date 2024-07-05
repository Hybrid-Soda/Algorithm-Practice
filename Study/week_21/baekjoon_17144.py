# 17144 미세먼지 안녕!

import sys
sys.stdin = open('input.txt')

dr = (0, 1), (1, 0), (0, -1), (-1, 0)
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
time = 0

def diffusion():
    temp = [[0] * C for _ in range(R)]
    # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    # 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
    # (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다
    for i in range(R):
        for j in range(C):
            out = room[i][j] // 5
            room[i][j] //= 5
            for di, dj in dr:
                temp[i+di][j+dj] += out
    
    for i in range(R):
        for j in range(C):
            

while True:
# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    diffusion()
    


# 공기청정기가 작동한다.
    # 공기청정기에서는 바람이 나온다.
    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.