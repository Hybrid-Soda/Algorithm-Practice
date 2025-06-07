# 14626 ISBN / 수학, 구현, 브루트포스 알고리즘, 사칙연산

isbn = input()
sum_num = 0
unknown_weight = 1
weight = [1, 3] * 6

for i in range(12):
    num = isbn[i]
    
    if num.isdigit():
        sum_num += int(num) * weight[i]
    else:
        unknown_weight = weight[i]

for i in range(10):
    rest = (sum_num + i*unknown_weight + int(isbn[-1])) % 10

    if rest == 0:
        exit(print(i))