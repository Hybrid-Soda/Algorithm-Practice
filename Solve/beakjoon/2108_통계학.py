# 2108 통계학 / 수학, 구현, 정렬, 집합과 맵

def get_mode(n, nums):
    modes = [nums[0]]
    mode_count = 0
    temp = 1

    for i in range(1, n):
        if nums[i] == nums[i-1]:
            temp += 1
        else:
            if temp > mode_count:
                modes = [nums[i-1]]
                mode_count = temp
            elif temp == mode_count:
                modes.append(nums[i-1])
            temp = 1
    if temp > mode_count:
        modes = [nums[-1]]
    elif temp == mode_count:
        modes.append(nums[-1])
    return modes[0] if len(modes) < 2 else modes[1]

n = int(input())
nums = sorted(int(input()) for _ in range(n))

print(round(sum(nums)/n))
print(nums[n//2])
print(get_mode(n, nums))
print(nums[-1] - nums[0])