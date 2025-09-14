# 11003_최솟값 찾기

from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque([])

for i in range(n):
    # 큐의 가장 작은 원소가 범위를 벗어났으면 제거
    if queue and queue[0][1] <= i-l:
        queue.popleft()

    # 새로 들어올 원소가 최솟값이면 앞의 원소 모두 제거
    while queue and arr[i] < queue[-1][0]:
        queue.pop()
    
    queue.append([arr[i], i])
    print(queue[0][0], end=" ")

# 시간 초과
# from heapq import heappop, heappush

# n, l = map(int, input().split())
# arr = list(map(int, input().split()))
# queue = []

# for i in range(n):
#     heappush(queue, [arr[i], i])

#     while queue[0][1] < i-l+1:
#         heappop(queue)
    
#     print(queue[0][0], end=" ")


# 기한이 만료된 숫자 제거
# 그 중 최소 숫자 골라내기
# 계속 최솟값 계산하기 빡셈
# 우선순위 큐 필요
# 필요한 것 : 값, 인덱스