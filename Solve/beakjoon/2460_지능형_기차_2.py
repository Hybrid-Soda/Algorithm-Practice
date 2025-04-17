# 2460 지능형 기차 2

p = 0
ans = 0

for _ in range(10):
    out_t, in_t  = map(int, input().split()) 
    p += in_t - out_t 
    ans = max(p, ans) 
    
print(ans)