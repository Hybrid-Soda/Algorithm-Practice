# 5355 화성 수학 / 수학, 구현, 사칙연산

for _ in range(int(input())):
    num, *equation = input().split()
    num = float(num)
    
    for s in equation:
        if s == '@':
            num *= 3.0
        elif s == '%':
            num += 5.0
        else:
            num -= 7.0
    
    print(f'{num:.2f}')