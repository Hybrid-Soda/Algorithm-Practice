# 1652 누울 자리를 찾아라 / 구현, 문자열

def find_spaces(room):
    h = v = 0

    for row in room:
        for s in row.split('X'):
            if len(s) >= 2:
                h += 1

    for col in zip(*room):
        for s in ''.join(col).split('X'):
            if len(s) >= 2:
                v += 1

    return h, v

n = int(input())
room = [input() for _ in range(n)]
h, v = find_spaces(room)
print(h, v)
