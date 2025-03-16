# 1459 걷기 / 수학, 많은 조건 분기

x, y, w, s = map(int, input().split())

if 2*w <= s:
    print((x+y)*w)
else:
    min_v = min(x, y)
    ans = min_v*s
    abs_v = abs(x-y)
    
    if w > s:
        if abs_v % 2 == 0:
            ans += abs_v*s
        else:
            ans += (abs_v-1)*s + w
    else:
        ans += abs_v*w
    
    print(ans)