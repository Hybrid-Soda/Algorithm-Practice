# 20006 랭킹전 대기열 / 구현, 시뮬레이션

p, m = map(int, input().split())
rooms = [[] for _ in range(300)]

for _ in range(p):
    level, name = input().split()
    level = int(level)

    for room in rooms:
        if not room or (len(room) < m and abs(room[0][0] - level) <= 10):
            room.append((level, name))
            break

for room in rooms:
    if not room:
        break

    print('Started!' if len(room) == m else 'Waiting!')
    for level, name in sorted(room, key=lambda x: x[1]):
        print(level, name)