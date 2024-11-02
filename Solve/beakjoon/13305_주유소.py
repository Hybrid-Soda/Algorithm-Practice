# 13305 주유소 / 그리디 알고리즘

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
now_cost = 1000000000
total_cost = 0

# 계단식 최소 지점 찾기
for i in range(N-1):
    now_cost = min(now_cost, costs[i])
    total_cost += now_cost * roads[i]

print(total_cost)