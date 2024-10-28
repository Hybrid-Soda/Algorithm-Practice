# 9017 크로스 컨트리 / 구현

# 팀당 6명, 상위 4명의 점수 합산
# 자격 : 6명이 참가해야 함, 6명 미만 팀 점수 계산에서 제외
# 조건 : 낮은 점수의 팀이 우승
# 동점 : 5번째 주자가 가장 빨리 들어온 팀 우승

for _ in range(int(input())):
    N = int(input())
    team_list = list(map(int, input().split()))
    team_dict = {}
    score_dict = {}

    # 1. 각 팀이 몇 명이 참가했는지 체크
    for i, team in enumerate(team_list):
        team_dict[team] = team_dict.get(team, []) + [i]

    # 2. 각 팀의 점수 체크
    score = 1
    for team in team_list:
        if len(team_dict[team]) == 6:
            score_dict[team] = score_dict.get(team, []) + [score]
            score += 1
    
    # 3. 우승 팀 판단
    min_team = 0
    min_score = 6000
    for team in score_dict.keys():
        # 총 점수 체크
        score_dict[team] = sum(score_dict[team][:4])
        
        # 3-1. 점수가 낮으면 업데이트
        if min_score > score_dict[team]:
            min_score = score_dict[team]
            min_team = team
        # 3-2. 점수가 같으면 5번째 주자가 몇 등인지 체크
        elif min_score == score_dict[team] and team_dict[team][4] < team_dict[min_team][4]:
            min_team = team

    print(min_team)