# 17298 오큰수 / 자료 구조, 스택

n = int(input())
a_list = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n):
    a = a_list[i]
    while stack and a > a_list[stack[-1]]:
        pi = stack.pop()
        ans[pi] = a
    stack.append(i)

while stack:
    i = stack.pop()
    ans[i] = -1

print(*ans)