# 10828 스택 / 구현, 자료 구조, 스택

stack = []

for _ in range(int(input())):
    cmd = input().split()

    if len(cmd) == 1:
        c = cmd[0]
        if c == 'pop':
            print(stack.pop() if stack else -1)
        elif c == 'size':
            print(len(stack))
        elif c == 'empty':
            print(0 if stack else 1)
        elif c == 'top':
            print(stack[-1] if stack else -1)
    else:
        stack.append(cmd[1])
