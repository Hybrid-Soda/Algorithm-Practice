# 1547 공 / 구현, 시뮬레이션

ball = [0, 1, 0, 0]

for i in range(int(input())):
    a, b = map(int, input().split())
    ball[a], ball[b] = ball[b], ball[a]

print(ball.index(1))