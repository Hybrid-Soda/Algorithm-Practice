# 10816 숫자 카드 2 / 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵

n, n_card = int(input()), list(map(int, input().split()))
m, m_card = int(input()), list(map(int, input().split()))
m_dict = {m_card[i]: 0 for i in range(m)}

for i in n_card:
    if i in m_dict:
        m_dict[i] += 1

for i in m_card:
    print(m_dict[i], end=' ')