# 15654 N과 M(5)

def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for n in serial:
        if n not in arr:
            dfs(arr + [n])

n, m = map(int, input().split())
serial = sorted(map(int, input().split()))

dfs([])