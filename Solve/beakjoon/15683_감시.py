# 15683 감시 / 구현, 브루트포스 알고리즘, 시뮬레이션, 백트래킹

def count_blind_spots(office):
    blind_spots = 0
    for i in range(n):
        for j in range(m):
            if office[i][j] == 0:
                blind_spots += 1
    return blind_spots

def fill(k, i, j, office):
    for d in k:
        ni, nj = i, j

        while True:
            ni += dir[d][0]
            nj += dir[d][1]
            if not (0<=ni<n and 0<=nj<m):
                break
            if office[ni][nj] == 6:
                break
            elif office[ni][nj] == 0:
                office[ni][nj] = -1

def deepcopy(office):
    new_office = []
    for row in office:
        new_office.append(row[:])
    return new_office

def dfs(depth, office):
    global ans
    if depth == len(cctv):
        ans = min(ans, count_blind_spots(office))
        return
    
    copied_office = deepcopy(office)
    num, i, j = cctv[depth]

    for k in mode[num]:
        fill(k, i, j, copied_office)
        dfs(depth+1, copied_office)
        copied_office = deepcopy(office)

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
ans = float('inf')

for i in range(n):
    for j in range(m):
        if office[i][j] in range(1, 6):
            cctv.append([office[i][j], i, j])

dfs(0, office)
print(ans)
