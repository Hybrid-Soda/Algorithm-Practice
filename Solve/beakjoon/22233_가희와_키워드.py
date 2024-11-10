# 22233 가희와 키워드 / 자료 구조, 문자열, 해시를 사용한 집합과 맵, 파싱

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {input().strip() for _ in range(n)}

for _ in range(m):
    keywords = input().strip().split(',')

    for keyword in keywords:
        # memo.discard(keyword) 도 가능
        if keyword in memo:
            memo.remove(keyword)
    
    print(len(memo))

# remove() : 실제 존재하는 대상을 지우는 동작에 사용
# discard() : 존재하지 않음을 보장하려고 할때 사용
