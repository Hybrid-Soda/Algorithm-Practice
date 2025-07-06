# 5635 생일 / 구현, 문자열, 정렬

younger = ['', 1, 1, 1990]
older = ['', 31, 12, 2010]

for i in range(int(input())):
    name, *date = input().split()
    day, month, year = map(int, date)
    yd, ym, yy = younger[1:]
    od, om, oy = older[1:]

    if ((yy < year) or
        (yy == year and ym < month) or
        (yy == year and ym == month and yd < day)):
        younger = [name, day, month, year]

    if ((oy > year) or
        (oy == year and om > month) or
        (oy == year and om == month and od > day)):
        older = [name, day, month, year]

print(younger[0])
print(older[0])