# 1780 종이의 개수

def check_same(paper, count):
    paper_set = set()

    for row in paper:
        paper_set.update(row)
    # print(paper)
    # print(paper_set)
    # print()

    if len(paper_set) > 1:
        for i in range(0, n+1, n//3):
            for j in range(0, n+1, n//3):
                check_same(paper[i:i+(n//3)][j:j+(n//3)], count)
    else:
        count[paper[0][0] + 1] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count = [0] * 3
print(paper[0:3][0:3])
check_same(paper, count)