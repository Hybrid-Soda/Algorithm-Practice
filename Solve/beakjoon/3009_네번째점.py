# 3009 네 번째 점 / 구현, 기하학

al, bl = set(), set()

for _ in range(3):
    a, b = input().split()

    if a not in al:
        al.add(a)
    else:
        al.remove(a)
    
    if b not in bl:
        bl.add(b)
    else:
        bl.remove(b)

print(al.pop(), bl.pop())