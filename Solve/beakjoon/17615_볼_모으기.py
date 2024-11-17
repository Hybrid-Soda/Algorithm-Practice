# 17615 볼 모으기 / 그리디 알고리즘

n = int(input())
balls = input()
cnt = []

r_right = balls.rstrip('R')
b_right = balls.rstrip('B')
r_left = balls.lstrip('R')
b_left = balls.lstrip('B')

cnt.append(r_right.count('R'))
cnt.append(b_right.count('B'))
cnt.append(r_left.count('R'))
cnt.append(b_left.count('B'))

print(min(cnt))

# 연속된 문자 제거하려면 strip() 사용하면 됨