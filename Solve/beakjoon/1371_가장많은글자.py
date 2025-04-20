# 1371 가장 많은 글자 / 구현, 문자열

freq = [0] * 26

try:
    while True:
        line = input()
        for ch in line:
            if 'a' <= ch <= 'z':
                freq[ord(ch) - ord('a')] += 1
except EOFError:
    pass

if sum(freq) == 0:
    exit()

max_freq = max(freq)
for i, count in enumerate(freq):
    if count == max_freq:
        print(chr(i + ord('a')), end='')

