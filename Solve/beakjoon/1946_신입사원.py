# 1946 신입 사원 / 정렬, 그리디 알고리즘

def compare_rank(n, rank):
    count = n
    best_rank = rank[0][1]

    for i in range(n):
        if rank[i][1] > best_rank:
            count -= 1
        else:
            best_rank = rank[i][1]

    return count

for _ in range(int(input())):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort(key=lambda x: x[0])
    print(compare_rank(n, rank))