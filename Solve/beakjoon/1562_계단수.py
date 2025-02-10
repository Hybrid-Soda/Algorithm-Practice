# 1562 계단 수 / 다이나믹 프로그래밍, 비트마스킹, 비트필드를 이용한 다이나믹 프로그래밍

n = int(input())
MOD = 1000000000

# dp[자리 수][마지막 숫자][사용된 숫자들의 비트 값] = 계단 수의 개수
dp = [[[0] * (1<<10) for _ in range(10)] for _ in range(n+1)]

# 길이가 1인 경우 초기화 (각 숫자 1~9는 각각 하나의 계단 수를 이룬다)
# 예시 : p[1][1][0b0000000010] = 1 -> 길이가 1이고 마지막 숫자가 1이며 숫자 1만 사용된 계단 수가 1개임을 의미
for d in range(1, 10):
    dp[1][d][1<<d] = 1

for l in range(2, n+1):
    for d in range(10):
        for b in range(1<<10):
            # 이전까지 사용된 숫자 + 현재 사용된 숫자 (OR연산)
            nb = b | (1<<d)

            if d > 0: # 마지막 숫자가 0보다 크면
                # 이전 숫자로 d-1이 올 수 있음
                dp[l][d][nb] += dp[l-1][d-1][b]
                dp[l][d][nb] %= MOD

            if d < 9: # 마지막 숫자가 9보다 작으면
                # 이전 숫자로 d+1이 올 수 있음
                dp[l][d][nb] += dp[l-1][d+1][b]
                dp[l][d][nb] %= MOD

# 길이가 n이고 모든 숫자를 사용한 경우의 수 합산 (bitmask == 1023)
result = 0
for d in range(10):
    result += dp[n][d][(1<<10) - 1]
    result %= MOD

print(result)