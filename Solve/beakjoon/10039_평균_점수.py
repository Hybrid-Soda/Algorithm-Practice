# 10039 평균 점수

nums = []

for _ in range(5):
    num = int(input())
    nums.append(max(num, 40))

print(sum(nums) // 5)