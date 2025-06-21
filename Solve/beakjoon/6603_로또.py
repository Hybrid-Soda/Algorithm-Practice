# 6603 로또 / 수학, 조합론, 백트래킹, 재귀

def lotto(arr, idx, cnt):
    if cnt == 6:
        print(*arr)
        return
    
    for i in range(idx, len(s)-1):
        arr[cnt] = s[i+1]
        lotto(arr, i+1, cnt+1)
    

while True:
    s = list(map(int, input().split()))
    
    if s[0] == 0: break
    
    lotto([0]*6, 0, 0)
    print()