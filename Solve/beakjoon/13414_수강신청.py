# 13414 수강신청 / 구현, 자료 구조, 해시를 사용한 집합과 맵

k, l = map(int, input().split())
nums = {}

for i in range(l):
    nums[input()] = i

sorted_nums = sorted(nums.items(), key=lambda x: x[1])

for i in range(k):
    if i < len(sorted_nums):
        print(sorted_nums[i][0])
    else:
        break