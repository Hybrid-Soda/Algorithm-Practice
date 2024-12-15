# 9935 문자열 폭발

hole_str = input()
boom_str = list(input())
n = len(boom_str)
stack = []

for char in hole_str:
    stack.append(char)

    if stack[len(stack)-n : len(stack)] == boom_str:
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')