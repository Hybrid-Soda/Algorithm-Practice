# 20125 쿠키의 신체 측정 / 구현

# 심장 위치 찾기
def find_heart(plate: list[str]) -> list[int]:
    for i in range(N):
        for j in range(N):
            # 머리를 찾았으면 한칸 아래의 심장 위치 저장
            if plate[i][j] == '*':
                return [i+1, j]

# 길이 카운트
def count(plate: list[str], start: list[int], r=0, d=0) -> int:
    length = 0
    i, j = start

    while True:
        i += d
        j += r
        if not(0<=i<N and 0<=j<N and plate[i][j] == '*'):
            break
        length += 1
    
    return length

N = int(input())
plate = [input() for _ in range(N)]
heart = find_heart(plate)
body = [0] * 5

# 심장에서부터 좌, 우, 하 로 계속 이동하며 '-'가 나올때까지 카운트
body[0] = count(plate, heart, r=-1)
body[1] = count(plate, heart, r=1)
body[2] = count(plate, heart, d=1)

# 하 맨끝에서는 대각선 아래의 좌우 부분에서 다시 하로 내려가며 카운트
leg_l = [heart[0]+body[2], heart[1]-1]
leg_r = [heart[0]+body[2], heart[1]+1]
body[3] = count(plate, leg_l, d=1)
body[4] = count(plate, leg_r, d=1)

# 출력
print(heart[0]+1, heart[1]+1)
print(*body)