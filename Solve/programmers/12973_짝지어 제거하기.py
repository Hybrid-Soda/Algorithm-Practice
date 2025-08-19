# 12973_짝지어 제거하기

def solution(s):
    stack = []

    for e in s:
        if stack and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)

    return 0 if stack else 1