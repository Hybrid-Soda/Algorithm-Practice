# 13144 List of Unique Numbers

n = int(input())
serial = list(map(int, input().split()))

start, end, answer = 0, 0, 0
visited = [False] * 100001

while end < n:
    if not visited[serial[end]]:
        visited[serial[end]] = True
        end += 1
        answer += end - start
    else:
        visited[serial[start]] = False
        start += 1

print(answer)
