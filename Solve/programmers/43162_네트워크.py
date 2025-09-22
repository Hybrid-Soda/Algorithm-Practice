def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                union(i, j, parent)

    for i in range(n):
        find(i, parent)

    return len(set(parent))

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x != y:
        parent[y] = x