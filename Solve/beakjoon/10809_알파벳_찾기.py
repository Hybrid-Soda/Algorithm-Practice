# 10809 알파벳 찾기

s = input()

for n in range(97, 123):
    char = chr(n)
    print(s.find(char), end=' ')