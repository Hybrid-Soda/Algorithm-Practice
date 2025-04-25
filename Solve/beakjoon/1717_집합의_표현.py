# 1717 집합의 표현 / 자료 구조, 분리 집합

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    comm, a, b = map(int, input().split())
    if comm:
        print('YES' if find(a) == find(b) else 'NO')
    else:
        union(a, b)