# 11747 수열 / 구현, 브루트포스 알고리즘

import sys

data = sys.stdin.read().split()
N = int(data[0])
digits = ''.join(data[1:1+N])

for i in range(int(10E8)):
    if str(i) not in digits:
        print(i)
        break