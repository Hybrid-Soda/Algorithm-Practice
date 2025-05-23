# 9375 패션왕 신해빈 / 수학, 자료 구조, 조합론, 해시를 사용한 집합과 맵, 집합과 맵

for _ in range(int(input())):
    wears = dict()
    n = int(input())

    for _ in range(n):
        name, type = input().split()
        wears[type] = wears.get(type, []) + [name]

    cnt = 1
    for x in wears:
        cnt *= (len(wears[x]) + 1)
    
    print(cnt-1)