# 16165 걸그룹 마스터 준석이 / 자료 구조, 해시를 사용한 집합과 맵, 집합과 맵

n, m = map(int, input().split())
gg_name = {}

for i in range(n):
    name = input()
    gg_member = []
    for u in range(int(input())):
        member = input()
        gg_member.append(member)
    gg_member.sort()
    gg_name[name] = gg_member

for i in range(m):
    quize = input()
    if int(input()) == 0:
        for m in gg_name[quize]:
            print(m)
    else:
        for a in gg_name.keys():
            if quize in gg_name[a]:
                print(a)