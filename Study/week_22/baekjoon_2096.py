# 2096 내려가기
N = int(input())
grid = list(map(int, input().split()))
minDP = grid[:]
maxDP = grid[:]

for _ in range(N-1):
    grid = list(map(int, input().split()))
    maxDP = [grid[0] + max(maxDP[0], maxDP[1]), grid[1] + max(maxDP), grid[2] + max(maxDP[1], maxDP[2])]
    minDP = [grid[0] + min(minDP[0], minDP[1]), grid[1] + min(minDP), grid[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))