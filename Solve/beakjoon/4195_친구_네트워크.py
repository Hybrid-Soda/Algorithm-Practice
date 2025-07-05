# 4195 친구 네트워크 / 자료 구조, 해시를 사용한 집합과 맵, 분리 집합, 집합과 맵

import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        visited[a] += visited[b]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def network(f):
    for _ in range(f):
        a, b = input().rstrip().split()

        if a not in parent:
            parent[a] = a
            visited[a] = 1

        if b not in parent:
            parent[b] = b
            visited[b] = 1

        union(a, b)
        print(visited[find(a)])

for _ in range(int(input())):
    f = int(input())
    parent = dict()
    visited = dict()
    network(f)