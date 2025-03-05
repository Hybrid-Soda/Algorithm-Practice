# 1439 뒤집기 / 그리디 알고리즘, 문자열

s = input()
cnt = 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cnt += 1

print(cnt//2)