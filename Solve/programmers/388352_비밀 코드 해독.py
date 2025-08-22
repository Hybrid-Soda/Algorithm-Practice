# 388352_비밀 코드 해독

from itertools import combinations

def solution(n, q, ans):
    answer = 0

    for candi in combinations(range(1, n+1), 5):
        answer += test(candi, q, ans)
    
    return answer

def test(candi, q, ans):
    for elem, cnt in zip(q, ans):
        inter_elem = len(set(candi).intersection(set(elem)))

        if inter_elem != cnt:
            return False
    
    return True