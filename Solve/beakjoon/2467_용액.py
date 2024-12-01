# 2467 용액 / 이분 탐색, 투 포인터

n = int(input())
fluids = list(map(int, input().split()))

left, right = 0, n - 1
min_value = float("inf")
ans = [0, 0]

# 두 포인터가 교차하기 전까지 반복
while left < right:
    value = fluids[left] + fluids[right]

    # 현재 합이 이전 최소값보다 절대값이 작으면 업데이트
    if min_value > abs(value):
        ans = [fluids[left], fluids[right]]
        min_value = abs(value)

    # 합이 0보다 크면 값을 줄이기 위해 오른쪽 포인터 이동
    if value > 0:
        right -= 1
    # 합이 0보다 작으면 값을 키우기 위해 왼쪽 포인터 이동
    elif value < 0:
        left += 1
    # 합이 0이면 최적이므로 반복 종료
    else:
        break

print(*ans)

# 1. "정렬된 배열"
# 문제에서 두 용액의 특성을 찾기 위해 정렬된 배열이 주어짐 → 정렬된 배열을 활용한 효율적인 탐색 가능

# 2. "두 수의 합"
# 두 용액의 특성을 더해 특정 값(0에 가까운 값)을 구해야 함 → 두 포인터 기법 활용 가능

# 3. "최적의 조합"
# 두 용액의 조합 중 가장 조건에 가까운 조합을 찾아야 함 → 탐색 과정에서 최적화된 비교 필요

# 4. "시간 복잡도 개선"
# 완전 탐색으로는 비효율적 → O(N) 또는 O(N log N) 알고리즘 필요
