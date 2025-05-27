# 9019 DSLR / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 역추적

from collections import deque

def fun_d(n):
    return n * 2 % 10000

def fun_s(n):
    return n - 1 if n > 0 else 9999

def fun_l(n):
    return (n % 1000) * 10 + (n // 1000)

def fun_r(n):
    return (n % 10) * 1000 + (n // 10)

go = {fun_d: 'D', fun_s: 'S', fun_l: 'L', fun_r: 'R'}

for _ in range(int(input())):
    a, b = map(int, input().split())
    queue = deque([(a, '')])
    visit = [0] * 10000
    visit[a] = 1
    
    while queue:
        now, cmd = queue.popleft()

        for fun in (fun_d, fun_s, fun_l, fun_r):
            res = fun(now)

            if res == b:
                print(cmd + go[fun])
                break

            if not visit[res]:
                queue.append((res, cmd + go[fun]))
                visit[res] = 1
        else:
            continue
        break
