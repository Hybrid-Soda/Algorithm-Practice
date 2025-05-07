# 28702 FizzBuzz / 수학, 문자열

nums = [input() for _ in range(3)]

for i in range(3):
    if nums[i].isdecimal():
        d = int(nums[i]) + 3 - i
        break

if d % 3 and d % 5:
    print(d)
elif d % 3:
    print("Buzz")
elif d % 5:
    print("Fizz")
else:
    print("FizzBuzz")