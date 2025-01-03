# 2179 비슷한 단어

n = int(input())
words = sorted((input(), i) for i in range(n))
ans_min_idx = 20000
prefix = ''

for i in range(n-1):
    w1, idx1 = words[i]
    w2, idx2 = words[i+1]

    min_idx = min(idx1, idx2)
    min_len = min(len(w1), len(w2))
    
    if w1 == w2: continue
    
    for j in range(min_len):
        if w1[j] != w2[j]:
            break
        j += (j == min_len - 1)

    # 현재 접두사가 더 길거나, 길이가 같고 인덱스가 더 작으면 갱신
    if len(prefix) < j or len(prefix) == j and min_idx < ans_min_idx:
        prefix = w1[:j]
        ans_min_idx = min_idx

# 접두사가 같은 단어들을 인덱스로 정렬
candidates = sorted((i, w) for w, i in words if w[:len(prefix)] == prefix)

for w in candidates[:2]:
    print(w[1])

'''
[보완해야 할 점]
- 공통 접두사를 탐색하는 문제로, 조건 갱신과 사전 순 정렬이 중요한 요소임.
- 인덱스를 기반으로 정렬하거나 조건을 다룰 때는 명확한 우선순위를 기준으로 코드를 작성해야 함.
'''