# 15651 N과 M (3) / 백트래킹

def dfs(serial):
    if len(serial) == m:
        print(*serial)
        return
    
    for i in range(1, n+1):
        serial.append(i)
        dfs(serial)
        serial.pop()

n, m = map(int, input().split())
dfs([])