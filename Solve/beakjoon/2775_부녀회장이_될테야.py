# 2775 부녀회장이 될테야 / 수학, 구현, 다이나믹 프로그래밍

for i in range(int(input())):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))
        people = new.copy()
    print(people[-1])