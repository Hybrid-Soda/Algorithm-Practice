# 383027 성적 평균

n, k = map(int, input().split())
score = [0] + list(map(int, input().split()))

for _ in range(k):
    a, b = map(int, input().split())
    avg = sum(score[a:b+1]) / (b-a+1)
    print(f'{avg:.2f}')