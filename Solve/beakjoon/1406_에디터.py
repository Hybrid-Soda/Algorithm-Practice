# 1406 에디터

string1 = list(input())
string2 = []

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'L':
        if string1:
            string2.append(string1.pop())
    elif cmd[0] == 'D':
        if string2:
            string1.append(string2.pop())
    elif cmd[0] == 'B':
        if string1:
            string1.pop()
    else:
        string1.append(cmd[1])

print(''.join(string1+string2[::-1]))

'''
    - 문제에서 커서 이동이 빈번히 일어나는 상황 → 리스트의 중간에서의 삽입/삭제는 비효율적
    - 커서를 기준으로 두 개의 스택으로 나누면 이동과 삭제/삽입 연산을 O(1)로 해결 가능
    - 이와 같은 문제는 연속된 데이터의 중간에서 빈번한 삽입/삭제가 있을 때 stack을 고려하는 것이 좋음
'''