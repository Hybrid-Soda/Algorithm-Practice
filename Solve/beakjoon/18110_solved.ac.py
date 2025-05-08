# 18110 solved.ac / 수학, 구현, 정렬

import sys
input = sys.stdin.readline

def round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)
    
n = int(input())
if n == 0:
    print(0)
else:
    scores = sorted([int(input()) for _ in range(n)])
    cut = round(n * 0.15)
    trimmed_scores = scores[cut: n-cut]
    result = round(sum(trimmed_scores) / len(trimmed_scores))
    print(result)