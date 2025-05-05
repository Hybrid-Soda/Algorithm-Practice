# 4949 균형잡힌 세상 / 자료 구조, 문자열, 스택

while True:
    string = input()
    y_or_n = 'yes'

    if string == '.':
        break

    stack = []
    for s in string:
        if s in ('(', '['):
            stack.append(s)
        elif stack and s in (')', ']'):
            if s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
            else:
                y_or_n = 'no'
                break
        elif not stack and s in (')', ']'):
            y_or_n = 'no'
            break
    if stack: y_or_n = 'no'

    print(y_or_n)