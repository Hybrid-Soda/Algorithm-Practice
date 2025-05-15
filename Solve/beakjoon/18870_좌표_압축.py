# 18870 좌표 압축 / 정렬, 값 / 좌표 압축

n = int(input())
x = list(map(int, input().split()))
dict_x = {n: i for i, n in enumerate(sorted(set(x)))}

for i in x:
    print(dict_x[i], end=' ')