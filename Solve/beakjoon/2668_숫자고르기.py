# 2668 숫자고르기 / 그래프 이론, 그래프 탐색, 깊이 우선 탐색


def dfs(now:int, start:int, visited: list):
    # 현재 노드를 방문 처리
    visited[now] = 1
    # 현재 노드에서 이동할 다음 노드를 가져옴
    next = nums[now]

    # 아직 방문하지 않은 노드라면, DFS 재귀 호출
    if not visited[next]:
        dfs(next, start, visited)
    # 방문한 노드이고, 그 노드가 시작 노드와 같다면 사이클을 찾은 것
    elif visited[next] and next == start:
        ans.append(next)


n = int(input())
nums = [-1] + [int(input()) for _ in range(n)]
ans = []

# 각 노드에 대해 DFS를 호출
for i in range(1, n+1):
    dfs(i, i, [0] * (n+1))

print(len(ans))
for i in sorted(ans):
    print(i)

# 핵심: 주어진 숫자 배열에서 사이클을 찾는 문제

# 해결 접근 방식

# 주어진 배열을 그래프처럼 이해:
# 숫자 배열을 통해 "이동 경로"를 제공하는 그래프처럼 생각
# 예를 들어, nums[i] 값은 노드 i에서 연결된 노드를 의미

# 사이클을 찾는 문제:
# 각 노드를 기준으로 DFS를 실행하여, 그 노드에서 시작해 다시 그 노드로 돌아오는지를 확인
# 이때, 방문을 관리하는 배열을 활용하여 이미 방문한 노드를 재방문하지 않도록 처리