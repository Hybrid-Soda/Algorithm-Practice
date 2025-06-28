# 10830 행렬 제곱 / 분할 정복, 재귀

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def cross(m1, m2):
    new_m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_m[i][j] += m1[i][k] * m2[k][j]
            new_m[i][j] %= 1000
    return new_m


def cal(n, b, a):
    if b == 1:
        return a
    elif b == 2:
        return cross(a, a)
    else:
        temp = cal(n, b//2, a)
        if b % 2 == 0:
            return cross(temp, temp)
        else:
            return cross(cross(temp, temp), a)

result = cal(n, b, matrix)

for c in result:
    for num in c:
        print(num % 1000, end=' ')
    print()