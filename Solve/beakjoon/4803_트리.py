# 4803 트리 / 자료 구조, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 분리 집합

from collections import deque

def get_tree_cnt(graph):
    pass


def main(tc):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    tree_cnt = get_tree_cnt(graph)

    if tree_cnt <= 0:
        print(f"Case {tc}: No trees.")
    elif tree_cnt == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {tree_cnt} trees.")


for tc in range(int(10e+9)):
    try:
        main(tc)
    except:
        break
