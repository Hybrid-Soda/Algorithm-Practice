# 5622 다이얼 / 구현

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in input():
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            result += num
print(result)