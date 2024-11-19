# 1522 문자열 교환

string = input() * 2
n = len(string) // 2
a_cnt = string.count('a') // 2
now_cnt = string[0:a_cnt].count('a')
max_cnt = 0

if a_cnt == n:
    exit(print(0))

for i in range(n+1):
    max_cnt = max(max_cnt, now_cnt)
    
    if string[i+a_cnt] == 'a':
        now_cnt += 1
    if string[i] == 'a':
        now_cnt -= 1

print(a_cnt - max_cnt)