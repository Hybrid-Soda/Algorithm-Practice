# 1138 한 줄로 서기 / 구현, 그리디 알고리즘

n = int(input())
info = list(map(int, input().split()))
sequence = [n]

for info_person in range(n-1, 0, -1):
    count = info[info_person-1]

    for j in range(len(sequence)+1):
        if count <= 0:
            sequence.insert(j, info_person)
            break

        if count > 0 and sequence[j] > info_person:
            count -= 1

print(*sequence)

# 키 큰 사람을 찾는 것이므로 끝부터 돌리면 됨