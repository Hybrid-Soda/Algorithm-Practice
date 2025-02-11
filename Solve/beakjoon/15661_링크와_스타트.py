# 15661 링크와 스타트

def get_team_stats(board):
    row_sums = [sum(row) for row in board]
    col_sums = [sum(col) for col in zip(*board)]
    combined_stats = [r + c for r, c in zip(row_sums, col_sums)]
    return sorted(combined_stats)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

stats = get_team_stats(board)
total = sum(stats) // 2

n //= 2
combi = [0]

# 앞쪽 절반(n개)에 대한 조합 합을 모두 구함
for i in stats[:n]:
    combi.extend([i + j for j in combi])

# 앞쪽 절반에 해당하는 합들로 만들 수 있는 것 체크
dp = [i in combi for i in range(total+1)]

# 뒤쪽 절반에 대해 점진적으로 체크 확장
for i in stats[n:]:
    dp[i:] = [a or b for a, b in zip(dp[i:], dp)]

# 가능한 합 중 가장 큰 값 찾아서 차이 출력
print(dp[::-1].index(True))