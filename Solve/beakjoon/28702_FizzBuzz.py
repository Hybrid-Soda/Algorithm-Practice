# 28702 FizzBuzz / 수학, 문자열

a, b, c = input(), input(), input()

if a.isdecimal():
    d = int(a) + 3
elif b.isdecimal():
    d = int(b) + 2
elif c.isdecimal():
    d = int(c) + 1

if d % 3 and d % 5:
    print(d)
elif d % 3:
    print("Buzz")
elif d % 5:
    print("Fizz")
else:
    print("FizzBuzz")