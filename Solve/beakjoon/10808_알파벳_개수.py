# 10808 알파벳 개수 / 구현, 문자열

s = input()
s_list = [0] * 26

for c in s:
    s_list[ord(c) - ord('a')] += 1

print(*s_list)