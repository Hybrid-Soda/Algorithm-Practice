# 1032 명령 프롬프트 / 구현, 문자열

n = int(input())
ans = list(input())

for _ in range(n-1):
    for i, char in enumerate(input()):
        if ans[i] != char:
            ans[i] = '?'

print(''.join(ans))