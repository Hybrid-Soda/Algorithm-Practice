# 10214 Baseball

for i in range(int(input())):
    y, k = map(int, input().split())
    
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")