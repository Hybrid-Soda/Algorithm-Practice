# 19637 IF문 좀 대신 써줘 / 이분 탐색
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
titles = [input().split() for _ in range(n)]

for _ in range(m):
    power = int(input())
    ans, left, right = 0, 0, n

    while left <= right:
        mid = (left+right) // 2

        if power <= int(titles[mid][1]):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(titles[ans][0])

# power가 titles[mid][1]보다 작거나 같으면, '답이 될 수 있는 후보'이므로 ans를 갱신하고 왼쪽 영역을 더 탐색
# 이분 탐색 문제를 풀 때 다음의 공식을 기억
'''
while left <= right:
    mid = (left + right) // 2
    
    if 조건:
        ans = mid
        right = mid - 1  # 더 작은 범위로 이동
    else:
        left = mid + 1  # 더 큰 범위로 이동
'''