# 20310 타노스 / 그리디 알고리즘, 문자열

s = input()
count_0 = s.count('0')
count_1 = len(s) - count_0

s = s.replace('1', '', count_1 // 2)
s = s[::-1].replace('0', '', count_0 // 2)
s = s[::-1]

print(s)