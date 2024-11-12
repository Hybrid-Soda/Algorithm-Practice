# 11501 주식 / 그리디 알고리즘

for _ in range(int(input())):
    n = int(input())
    stock_prices = list(map(int, input().split()))
    profit = 0
    local_max = 0

    for price in stock_prices[::-1]:
        if price > local_max:
            local_max = price
        else:
            profit += local_max - price
    
    print(profit)
