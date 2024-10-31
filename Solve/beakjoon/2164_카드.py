# 2164 카드 / 자료구조, 큐

# 1번 방법 =========================
from collections import deque

N = int(input())
if N == 1: exit(print(1))

Q = deque([i for i in range(1, N+1)])
while Q:
    _ = Q.popleft()
    n = Q.popleft()
    
    if len(Q) > 0:
        Q.append(n)
    else:
        print(n)

# 2번 방법 ==========================

N = int(input())
P = 2

if N in (1, 2):
    print(N)
else:
    while P < N:
        P *= 2
    print((N - (P // 2)) * 2)