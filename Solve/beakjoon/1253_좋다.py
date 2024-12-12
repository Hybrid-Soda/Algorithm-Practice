# 1253 좋다 / 정렬, 이분탐색, 투 포인터


def two_pointer(idx: int, nums: list[int]):
    temp_nums = nums[:idx] + nums[idx + 1 :]
    left, right = 0, len(temp_nums) - 1

    while left < right:
        sum_num = temp_nums[left] + temp_nums[right]

        if sum_num > nums[idx]:
            right -= 1
        elif sum_num < nums[idx]:
            left += 1
        else:
            return 1
    return 0


n = int(input())
nums = sorted(map(int, input().split()))
ans = 0

for i in range(n):
    ans += two_pointer(i, nums)

print(ans)

# 주어지는 수의 범위 잘 보기 (양수, 음수)
