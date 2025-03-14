# 3015 오아시스 재결합 / 자료 구조, 스택

stack = []
ans = 0

for _ in range(int(input())):
    h = int(input())
    cnt = 1
    
    # 스택이 비어있지 않고, 현재 높이가 스택 top보다 큰 경우
    while stack and stack[-1][0] < h:
        ans += stack[-1][1]
        stack.pop()
    
    # 스택이 비어있지 않고, 현재 높이와 같은 경우
    if stack and stack[-1][0] == h:
        # 같은 높이의 사람 수만큼 쌍 추가
        ans += stack[-1][1]
        cnt += stack[-1][1]
        stack.pop()
    
    # 스택이 비어있지 않은 경우 (자신보다 큰 사람이 있는 경우)
    if stack:
        ans += 1
    
    # 현재 높이와 카운트를 스택에 추가
    stack.append((h, cnt))

print(ans)