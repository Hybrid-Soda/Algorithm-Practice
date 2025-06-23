# 1912 연속합 / 다이나믹 프로그래밍, 최대 부분 배열 문제

n = int(input())
numbers = list(map(int,input().split()))

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i]+numbers[i-1])

print(max(numbers))