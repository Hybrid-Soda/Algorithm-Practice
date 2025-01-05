# 4179 불!

from collections import deque

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]

queue = deque()
dir = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i in range(r):
    for j in range(c):
        # 지훈이의 위치와 시간을 큐에 추가
        if maze[i][j] == 'J':
            maze[i][j] = 0
            queue.append([i, j, 0])
        # 불의 위치를 큐의 앞에 추가
        elif maze[i][j] == 'F':
            maze[i][j] = '#'
            queue.appendleft([i, j, 'F'])

while queue:
    i, j, val = queue.popleft()

    # 지훈이가 미로의 가장자리에 도달한 경우 종료
    if isinstance(val, int) and (i in (0, r-1) or j in (0, c-1)):
        print(val + 1)
        exit()

    for di, dj in dir:
        ni, nj = i + di, j + dj
        
        if 0<=ni<r and 0<=nj<c:
            if val == 'F' and maze[ni][nj] != '#':
                maze[ni][nj] = "#" 
                queue.append([ni, nj, 'F'])
            elif isinstance(val, int) and maze[ni][nj] == '.':
                maze[ni][nj] = val + 1
                queue.append([ni, nj, val + 1])

print('IMPOSSIBLE')
