# 9012 괄호 / 자료 구조, 문자열, 스택

for _ in range(int(input())):
    ps = input()
    stack = []

    for s in ps:
        if stack and stack[-1] == '(' and s == ')':
            stack.pop()
        else:
            stack.append(s)

    print('NO' if stack else 'YES')