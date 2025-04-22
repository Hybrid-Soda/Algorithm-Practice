# 10250 ACM 호텔 / 수학, 구현, 사칙연산

for _ in range(int(input())):
    h, w, n = map(int, input().split( ))
    floor = n % h 
    room_line = n // h + 1

    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)