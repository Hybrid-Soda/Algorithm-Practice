# 7568 덩치 / 구현, 브루트포스 알고리즘
def compare(now, next):
    if now[0] < next[0] and now[1] < next[1]:
        return 1
    elif now[0] > next[0] and now[1] > next[1]:
        return 2
    return 0

N = int(input())
size = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N):
    for j in range(i, N):
        res = compare(size[i], size[j])
        if res == 1:
            rank[i] += 1
        elif res == 2:
            rank[j] += 1
    
print(*rank)

# 브루트포스 사용 이유
# 1. 모든 쌍 비교가 필요함: 각 사람의 몸무게와 키를 나머지 사람들과 비교해 "더 큰 덩치"를 찾는 과정이 필요함.
# 2. 시간 복잡도 문제 없음: 최대 N이 50이므로, O(N^2) 시간 복잡도의 브루트 포스 알고리즘으로도 충분히 해결 가능함.
# 3. 단순한 규칙: 각 사람을 기준으로 나머지 사람과 비교해 덩치 등수를 계산하는 단순 비교 작업이므로, 복잡한 자료구조나 고급 알고리즘이 필요하지 않음.