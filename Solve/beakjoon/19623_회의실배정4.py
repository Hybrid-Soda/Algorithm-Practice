# 19623 회의실 배정 4

import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

dp = [0] * n
dp[0] = arr[0][2]

end_time = [arr[i][1] for i in range(n)]

for i in range(1, n):
    # 현재 회의의 시작 시간보다 이전에 끝나는 회의 중 가장 늦게 끝나는 회의를 찾음
    idx = bisect_right(end_time, arr[i][0], 0, i) - 1

    # 이전 회의가 존재하면, 그 회의를 포함한 경우와 포함하지 않은 경우 중 최대 이익을 선택
    if idx != -1:
        dp[i] = max(dp[i - 1], dp[idx] + arr[i][2])
    else:
        dp[i] = max(dp[i - 1], arr[i][2])

print(dp[n - 1])

# -----------------------

# def bisect_right_custom(arr, target, lo=0, hi=None):
#     if hi is None:
#         hi = len(arr)
    
#     while lo < hi:
#         mid = (lo + hi) // 2
#         if arr[mid] > target:
#             hi = mid
#         else:
#             lo = mid + 1

#     return lo

# arr: 정렬된 배열
# target: 탐색할 값
# lo, hi: 탐색할 범위 (lo는 기본값 0, hi는 기본적으로 배열의 길이)