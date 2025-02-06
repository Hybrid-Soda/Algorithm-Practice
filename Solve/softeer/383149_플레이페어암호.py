# 383149 플레이페어 암호

msg = input()
key = input()

visit = [0] * (ord('Z') + 1)
matrix = [[None] * 5 for _ in range(5)]

# 5x5 크기의 표로 변환
idx = 0
for c in key:
    num = ord(c)
    if not visit[num]:
        matrix[idx//5][idx%5] = c
        visit[num] = 1
        idx += 1

for num in range(ord('A'), ord('Z')+1):
    if not visit[num] and num != ord('J'):
        matrix[idx//5][idx%5] = chr(num)
        visit[num] = 1
        idx += 1

# 메세지를 두 글자로 나눔
idx = 0
new_msg = ''
while idx < len(msg)-1:
    if msg[idx] == msg[idx+1]:
        new_msg += msg[idx] + ('Q' if msg[idx] == 'X' else 'X')
        idx += 1
    else:
        new_msg += msg[idx:idx+2]
        idx += 2

if idx == len(msg)-1:
    new_msg += msg[idx]

if len(new_msg) % 2:
    new_msg += 'X'

# 메세지 암호화
def search(c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j

encoded_msg = ''
for i in range(0, len(new_msg), 2):
    a, b = new_msg[i:i+2]
    ai, aj = search(a)
    bi, bj = search(b)
    
    if ai == bi:
        aj = (aj+1) % 5
        bj = (bj+1) % 5
    elif aj == bj:
        ai = (ai+1) % 5
        bi = (bi+1) % 5
    else:
        aj, bj = bj, aj

    encoded_msg += matrix[ai][aj] + matrix[bi][bj]

print(encoded_msg)
