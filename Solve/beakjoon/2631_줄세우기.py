# 2631 줄세우기 / 다이나믹 프로그래밍

n = int(input())
children = [int(input()) for _ in range(n)]

# 각 위치에서의 최장 증가 부분 수열의 길이를 저장할 배열
dp = [1] * n

for i in range(n):
    for j in range(i):
        
        # 현재 아이가 이전 아이보다 번호가 크다면 갱신
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 전체 아이들 수에서 최장 증가 부분 수열의 길이를 빼서 이동해야 하는 최소 아이들 수 출력
print(n - max(dp))

'''
최장 증가 부분 수열(LIS, Longest Increasing Subsequence)

[문제 구조 이해]
- 이동하는 아이들의 수 최소화 = 이동하지 않아도 되는 아이들의 수 최대화
- 이동하지 않아도 되는 아이들의 순서는 증가하는 순서여야 함
- 즉, 문제의 핵심은 주어진 배열에서 증가하는 부분 수열 중 가장 긴 수열(LIS)을 찾는 것
'''