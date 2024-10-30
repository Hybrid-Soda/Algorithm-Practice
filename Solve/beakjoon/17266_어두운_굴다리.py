# 17266 어두운 굴다리 / 구현, 이분탐색

N = int(input())
M = int(input())
lights = list(map(int, input().split()))
min_height = lights[0]

if M == 1:
    print(max(min_height, N-min_height))
    exit()

for i, light in enumerate(lights):
    if i == M-1:
        min_height = max(N-light, min_height)
    elif i != 0:
        min_height = max(-((lights[i-1] - light)//2), min_height)

print(min_height)