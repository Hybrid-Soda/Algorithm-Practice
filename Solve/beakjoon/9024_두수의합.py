# 9024 두 수의 합 / 정렬, 이분 탐색, 두 포인터

import sys
input = sys.stdin.readline

def two_pointer(n: int, k: int, arr: list):
    left, right = 0, n - 1
    min_term = float('inf')
    cnt = 0

    # 두 포인터를 사용하여 배열의 두 수의 합이 k와 가장 가까운 경우의 수를 찾음
    while left < right:
        num_sum = arr[left] + arr[right]
        term = abs(num_sum - k)

        # 현재 차이가 최소 차이보다 작으면 갱신
        if min_term > term:
            min_term = term
            cnt = 1
        # 현재 차이가 최소 차이와 같으면 경우의 수 증가
        elif min_term == term:
            cnt += 1

        # 두 수의 합이 k보다 작거나 같으면 왼쪽 포인터 증가
        if num_sum <= k:
            left += 1
        # 두 수의 합이 k보다 크면 오른쪽 포인터 감소
        else:
            right -= 1

    return cnt

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    print(two_pointer(n, k, arr))