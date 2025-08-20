# 389479_서버 증설 횟수

def solution(players, m, k):
    answer = 0
    servers = []

    # 시뮬레이션 시작
    for users in players:
        # 증설이 필요한 서버 개수 체크
        servers_req = users // m
        diff = servers_req - len(servers)

        # 현재 서버 개수와 비교해 부족하면 증설 + 증설된 서버 개수 체크
        if diff > 0:
            servers.extend([k] * diff)
            answer += diff

        # 서버 별로 순회하면서 남은 시간 차감
        d = -1
        for i in range(len(servers)):
            servers[i] -= 1

            if servers[i] <= 0:
                d = i

        # 남은 시간이 0인 서버 축소
        servers = servers[d+1:]

    return answer
