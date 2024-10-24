# 8979 올림픽

N, K = map(int, input().split())
m_list = []
m_dict = {}

for _ in range(N):
    C, *c_list = map(int, input().split())
    m_list.append(c_list)
    m_dict[C] = c_list

m_list.sort(reverse=True)
print(m_list.index(m_dict[K])+1)


# 저장할 것 : 메달 수, 등수
# 정렬 할 필요 없고 등수만 알면 되므로 본인 이상의 나라만 체크하면 된다.
# list의 index 메서드는 가장 먼저 나온 요소의 인덱스를 반환
