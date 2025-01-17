# 10989 수 정렬하기 3

n = int(input())
nums = [0] * 10001

for _ in range(n):
    nums[int(input())] += 1

for i in range(1, 10001):
    for _ in range(nums[i]):
        print(i)