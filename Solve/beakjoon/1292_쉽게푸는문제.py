# 1292 쉽게 푸는 문제 / 수학, 구현

a, b = map(int, input().split())
nums = [0]

for i in range(1, b+1):
    nums.extend([i] * i)
    if len(nums) > b:
        break

print(sum(nums[a:b+1]))
