# 19941 햄버거 분배 / 그리디 알고리즘

from collections import deque

def check(i, ans, queue_1, queue_2):
    while queue_1:
        idx = queue_1.popleft()
        if i - idx <= K:
            ans += 1
            break
    else:
        queue_2.append(i)
    return ans

N, K = map(int, input().split())
string = input()
h_queue = deque([])
p_queue = deque([])
ans = 0

for i in range(N):
    if string[i] == 'H':
        ans = check(i, ans, p_queue, h_queue)
    else:
        ans = check(i, ans, h_queue, p_queue)

print(ans)
