# 15649 N과 M (1)

def dfs(depth, stack, visit):
    if depth == m:
        print(*stack)
        return
    
    for i in range(1, n+1):
        if visit[i]: continue
        
        visit[i] = 1
        dfs(depth+1, stack + [i], visit)
        visit[i] = 0

n, m = map(int, input().split())
dfs(0, [], [0] * (n+1))