# 1780 종이의 개수

def check_same(paper, count, n):
    m = n//3
    paper_set = set()

    for row in paper:
        paper_set.update(row)
    
    num_cnt = len(paper_set)

    if num_cnt > 1:
        for i in range(0, n, m):
            for j in range(0, n, m):
                check_same([paper[k][j:j+m] for k in range(i, i+m)], count, m)
    elif num_cnt == 1:
        count[paper_set.pop() + 1] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count = [0] * 3
check_same(paper, count, n)

for i in count:
    print(i)