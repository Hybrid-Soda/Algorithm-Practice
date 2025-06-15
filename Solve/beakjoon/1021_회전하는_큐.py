# 1021 회전하는 큐 / 자료 구조, 덱

from collections import deque

n, m = map(int, input().split())
out_list = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])
count = 0
i = 0

while i < m:
    if out_list[i] == q[0]:
        q.popleft()
        i += 1
    else:
        mid = int(len(q) / 2)
        if q.index(out_list[i]) <= mid:
            temp = q.popleft()
            q.append(temp)
            count += 1
        else:
            temp = q.pop()
            q.appendleft(temp)
            count += 1

print(count)