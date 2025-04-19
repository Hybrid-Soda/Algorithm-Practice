# 5397 키로거 / 자료 구조, 스택, 연결 리스트

for _ in range(int(input())):
    line = input()
    left_stack = []
    right_stack = []

    for ch in line:
        if ch == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif ch == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif ch == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(ch)

    result = ''.join(left_stack) + ''.join(reversed(right_stack))
    print(result)