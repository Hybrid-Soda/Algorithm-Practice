# 3806 S를 T로 / 그리디 알고리즘

def inspect(s, t):
    cnt0, cnt1, cntq0, cntq1 = 0, 0, 0, 0

    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] == '0':
            cnt0 += 1
        elif s[i] == '1':
            cnt1 += 1
        elif t[i] == '0':
            cntq0 += 1
        else:
            cntq1 += 1

    if cnt1 > cnt0 + cntq1:
        return -1

    if cnt1 > cnt0:
        return cnt1 + cntq0 + cntq1

    return cnt0 + cntq0 + cntq1


for tc in range(int(input())):
    s = input()
    t = input()
    print(f'Case {tc+1}:', inspect(s, t))