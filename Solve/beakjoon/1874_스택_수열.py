# 1874 스택 수열

n = int(input())
serial = [int(input()) for _ in range(n)]
stack = []
ans = []

idx = 0
for i in range(1, n+1):
    stack.append(i)
    ans.append('+')

    while stack and idx < n and serial[idx] == stack[-1]:
        stack.pop()
        idx += 1
        ans.append('-')

if stack:
    print('NO')
else:
    for i in ans:
        print(i)