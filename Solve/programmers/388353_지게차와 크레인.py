# 388353_지게차와 크레인

dir = (1, 0), (0, 1), (-1, 0), (0, -1)

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    storage = [[0] * (m+2)] + list(map(lambda x: [0] + list(x) + [0], storage)) + [[0] * (m+2)]
    answer = n * m

    for request in requests:
        # request의 글자수 파악 > 1개면 지게차, 2개면 크레인
        is_fork = False if len(request) == 2 else True

        # 남은 컨테이너에서 감산
        if is_fork:
            answer -= oper_fork(request, storage, n+2, m+2)
        else:
            answer -= oper_crane(request[0], storage, n, m)

    return answer

# 지게차는 겉면에 노출된 알파벳만 제거 후 0으로 수정 (dfs)
def oper_fork(chr, storage, n, m):
    cnt = 0
    stack = [[0, 0]]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while stack:
        i, j = stack.pop()

        for di, dj in dir:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = True
                if storage[ni][nj] == 0:
                    stack.append([ni, nj])
                elif storage[ni][nj] == chr:
                    storage[ni][nj] = 0
                    cnt += 1

    return cnt

# 크레인은 모든 알파벳 제거 후 0으로 수정
def oper_crane(chr, storage, n, m):
    cnt = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if storage[i][j] == chr:
                storage[i][j] = 0
                cnt += 1
    
    return cnt
