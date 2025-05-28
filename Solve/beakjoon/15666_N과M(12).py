# 15666 N과 M (12) / 백트래킹

def solve(depth, idx):
    if depth == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(idx, len(k)):
        ans.append(k[i])
        solve(depth+1, i)
        ans.pop()

n, m = map(int, input().split())
k = sorted(set(map(int, input().split())))
ans = []
solve(0, 0)