# 2108 통계학

def get_mode(nums):
    modes = [nums[0]]
    mode_count = 1
    temp = 1

    for i in range(1, n):
        if nums[i] == nums[i-1]:
            temp += 1
        else:
            if temp > mode_count:
                modes = [nums]
            elif temp == mode_count:
                modes.append(nums[i-1])
            else:
                temp = 1
    
    return modes[0] if len(modes) < 2 else modes[1]

n = int(input())
nums = sorted(int(input()) for _ in range(n))

print(sum(nums)//n)
print(nums[n//2])
print(get_mode)
print(nums[-1] - nums[0])