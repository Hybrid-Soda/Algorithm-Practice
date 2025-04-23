# 16968 차량 번호판 1

n = input()
ans = 10 if n[0] == 'd' else 26

for i in range(1, len(n)):
    if n[i] == 'd':
        ans *= 9 if n[i-1] == 'd' else 10
    elif n[i] == 'c':
        ans *= 25 if n[i-1] == 'c' else 26

print(ans)