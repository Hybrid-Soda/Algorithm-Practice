# 2579 계단 오르기

n = int(input())
nums = list(int(input()) for _ in range(n))
dp = [[0, 0] for _ in range(n+1)]  # 이전 계단 안 밟음, 밟음
dp[1][0] = nums[0]

for i in range(2, n+1):
    # 이전 계단을 밟지 않은 경우
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + nums[i-1]
    # 이전 계단을 밟은 경우 (3연속 불가능)
    dp[i][1] = dp[i-1][0] + nums[i-1]

print(max(dp[-1]))