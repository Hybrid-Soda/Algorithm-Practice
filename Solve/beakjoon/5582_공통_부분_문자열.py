# 5582 공통 부분 문자열 / 다이나믹 프로그래밍, 문자열

str_1 = input()
str_2 = input()
n, m = len(str_1), len(str_2)

dp = [[0] * m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if str_1[i] == str_2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)

# 두 문자열의 모든 인덱스 조합을 고려해야 함
# 각 문자열의 인덱스를 상태로 활용하여 dp 배열의 차원을 구성
# 현재 문자가 일치하면 이전 인덱스(dp[i-1][j-1])의 결과에 1을 더하는 점화식을 구성